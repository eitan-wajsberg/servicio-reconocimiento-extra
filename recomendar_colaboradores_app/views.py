import json
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Colaborador, Recomendacion
from .serializers import ColaboradorSerializer, SolicitanteSerializer, SolicitudSerializer, RecomendacionSerializer
from datetime import timedelta
from django.utils import timezone

logger = logging.getLogger(__name__)

class RecomendarColaboradoresAPIView(APIView):
    def post(self, request):
        try:
            # Obtener parámetros desde el cuerpo de la solicitud
            puntos_minimos = int(request.data.get('puntos_minimos', 0))
            donaciones_minimas = int(request.data.get('donaciones_minimas', 0))
            max_colaboradores = int(request.data.get('max_colaboradores', 10))
            
            # Datos del solicitante desde el body
            solicitante_data = request.data.get('solicitante', {})

            # Verifica si el solicitante es un diccionario
            if not isinstance(solicitante_data, dict):
                return Response({'error': 'El campo "solicitante" debe ser un diccionario.'}, status=status.HTTP_400_BAD_REQUEST)

            # Datos de la solicitud
            solicitud_data = {
                'cant_min_puntos': puntos_minimos,
                'cant_min_viandas_ultimo_mes': donaciones_minimas,
                'fecha': timezone.now().date(),
                'cant_max_colaboradores': max_colaboradores,
                'solicitante': None  # Se establecerá más adelante
            }

            # Obtener colaboradores basados en los parámetros
            colaboradores_data = request.data.get('colaboradores', [])

            # Filtrar los colaboradores en base a los parámetros dados
            colaboradores_instancias = []
            for col_data in colaboradores_data:
                if col_data['puntaje_neto'] >= puntos_minimos and col_data['cantidad_viandas_ultimo_mes'] >= donaciones_minimas:
                    # Buscar si el colaborador ya existe en la base de datos
                    colaborador = Colaborador.objects.filter(
                        tipo_documento=col_data.get('tipo_documento'),
                        nro_documento=col_data.get('nro_documento')
                    ).first()
                    
                    if colaborador:
                        # Actualizar el colaborador existente con nuevos datos
                        for attr, value in col_data.items():
                            setattr(colaborador, attr, value)
                        colaborador.save()
                    else:
                        # Crear un nuevo colaborador si no existe
                        colaborador_serializer = ColaboradorSerializer(data=col_data)
                        if colaborador_serializer.is_valid():
                            colaborador = colaborador_serializer.save()
                        else:
                            return Response(colaborador_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
                    colaboradores_instancias.append(colaborador)

            # Limitar el número de colaboradores según max_colaboradores
            colaboradores_instancias = sorted(colaboradores_instancias, key=lambda x: x.puntaje_neto, reverse=True)[:max_colaboradores]

            # Verifica si se encontraron colaboradores
            if not colaboradores_instancias:
                return Response({'error': 'No se encontraron colaboradores con los criterios especificados.'}, status=status.HTTP_404_NOT_FOUND)

            # Serializa los colaboradores filtrados
            colaborador_serializer = ColaboradorSerializer(colaboradores_instancias, many=True)

            # Crear y guardar el solicitante
            solicitante_serializer = SolicitanteSerializer(data=solicitante_data)
            if solicitante_serializer.is_valid():
                solicitante = solicitante_serializer.save()
            else:
                return Response(solicitante_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # Actualizar solicitud_data con el solicitante creado
            solicitud_data['solicitante'] = solicitante_data

            # Crear y guardar la solicitud
            solicitud_serializer = SolicitudSerializer(data=solicitud_data)
            if solicitud_serializer.is_valid():
                solicitud = solicitud_serializer.save()
            else:
                return Response(solicitud_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Crear y guardar la recomendación
            recomendacion = Recomendacion.objects.create(
                solicitud=solicitud,
                fecha_recomendacion=timezone.now()
            )
            recomendacion.colaboradores.set(colaboradores_instancias)  # Usa las instancias de Colaborador
            recomendacion.save()

            return Response({
                'message': 'Solicitud, Solicitante, y Recomendación guardados exitosamente.',
                'data': {
                    'solicitante': solicitante_serializer.data,
                    'solicitud': solicitud_serializer.data,
                    'colaboradores': colaborador_serializer.data,
                    'recomendacion': {
                        'id': recomendacion.id,
                        'fecha_recomendacion': recomendacion.fecha_recomendacion
                    }
                }
            }, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e), 'data': request.data}, status=status.HTTP_400_BAD_REQUEST)
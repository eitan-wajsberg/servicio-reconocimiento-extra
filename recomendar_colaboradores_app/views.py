import json
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Colaborador
from .serializers import ColaboradorSerializer
from datetime import timedelta
from django.utils import timezone

logger = logging.getLogger(__name__)

class RecomendarColaboradoresAPIView(APIView):
    def get(self, request):
        # Función auxiliar para obtener parámetros de consulta con valores predeterminados
        def get_query_param(param_name, default_value, cast_type):
            try:
                return cast_type(request.query_params.get(param_name, default_value))
            except ValueError:
                raise ValueError(f'El parámetro "{param_name}" debe ser de tipo {cast_type.__name__}.')

        try:
            puntos_minimos = get_query_param('puntos_minimos', 0, int)
            donaciones_minimas = get_query_param('donaciones_minimas', 0, int)
            max_colaboradores = get_query_param('max_colaboradores', 10, int)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        # Filtrar colaboradores basado en los parámetros
        colaboradores = Colaborador.objects.filter(
            puntaje_neto__gte=puntos_minimos,
            cantidad_viandas_ultimo_mes__gte=donaciones_minimas
        ).order_by('-puntaje_neto')[:max_colaboradores]
        
        # Serializar los colaboradores filtrados
        serializer = ColaboradorSerializer(colaboradores, many=True)
    
        return Response({
            'message': 'Colaboradores recomendados obtenidos exitosamente.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ColaboradorSerializer(data=request.data, many=True)

        logger.debug('Serializer initialized: %s', serializer)

        if serializer.is_valid():
            serializer.save()
            logger.debug('Serializer data: %s', serializer.data)
            return Response({
                'message': 'Colaboradores guardados exitosamente.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            logger.debug('Serializer errors: %s', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
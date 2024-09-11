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
        try:
            puntos_minimos = int(request.query_params.get('puntos_minimos', 0))
            donaciones_minimas = int(request.query_params.get('donaciones_minimas', 0))
            max_colaboradores = int(request.query_params.get('max_colaboradores', 10))
        except ValueError:
            return Response({'error': 'Parámetros inválidos.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Filtro de colaboradores basado en parámetros.
        colaboradores = Colaborador.objects.filter(
            puntaje_neto__gte=puntos_minimos,
            cantidad_viandas_ultimo_mes__gte=donaciones_minimas
        ).order_by('-puntaje_neto')[:max_colaboradores]
        
        # Serialización de los colaboradores filtrados.
        serializer = ColaboradorSerializer(colaboradores, many=True)
        
        return Response({
            'message': 'Colaboradores recomendados obtenidos exitosamente.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request): 
        # Inicializar el serializador con el diccionario de Python
        serializer = ColaboradorSerializer(data=request, many=True)
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

""" try:
        data = json.loads(request)
        except json.JSONDecodeError:
            logger.debug('JSON Decode Error: %s', request)
            return Response({'error': 'JSON inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        logger.debug('Request data: %s', data)
"""
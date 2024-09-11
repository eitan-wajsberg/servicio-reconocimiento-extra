from rest_framework import serializers
from .models import Colaborador, Solicitud, Solicitante, Recomendacion

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'

class SolicitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitante
        fields = ['id', 'razon_social', 'rubro', 'whatsapp', 'mail', 'user_telegram', 'direccion']

class SolicitudSerializer(serializers.ModelSerializer):
    solicitante = SolicitanteSerializer()  # Embed SolicitanteSerializer

    class Meta:
        model = Solicitud
        fields = ['id', 'cant_min_puntos', 'cant_min_viandas_ultimo_mes', 'fecha', 'cant_max_colaboradores', 'solicitante']

class RecomendacionSerializer(serializers.ModelSerializer):
    colaboradores_recomendados = ColaboradorSerializer(many=True)  # Embed ColaboradorSerializer
    solicitud = SolicitudSerializer()  # Embed SolicitudSerializer

    class Meta:
        model = Recomendacion
        fields = ['id', 'solicitud', 'colaboradores', 'fecha_recomendacion']



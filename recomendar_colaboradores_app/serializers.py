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
    solicitante = SolicitanteSerializer()  # El solicitante es un serializer anidado

    class Meta:
        model = Solicitud
        fields = ['cant_min_puntos', 'cant_min_viandas_ultimo_mes', 'fecha', 'cant_max_colaboradores', 'solicitante']

    def create(self, validated_data):
        # Extraer los datos del solicitante del validated_data
        solicitante_data = validated_data.pop('solicitante')

        # Crear el solicitante usando el solicitante_serializer
        solicitante = Solicitante.objects.create(**solicitante_data)

        # Crear la solicitud con el solicitante que acabamos de crear
        solicitud = Solicitud.objects.create(solicitante=solicitante, **validated_data)

        return solicitud

class RecomendacionSerializer(serializers.ModelSerializer):
    colaboradores_recomendados = ColaboradorSerializer(many=True)  # Embed ColaboradorSerializer
    solicitud = SolicitudSerializer()  # Embed SolicitudSerializer

    class Meta:
        model = Recomendacion
        fields = ['id', 'solicitud', 'colaboradores', 'fecha_recomendacion']



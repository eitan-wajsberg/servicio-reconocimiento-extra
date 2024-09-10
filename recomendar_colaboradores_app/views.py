from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Colaborador
from .serializers import ColaboradorSerializer
from datetime import timedelta

class RecomendarColaboradoresAPIView(APIView):
    def get(self, request):
        puntos_minimos = int(request.query_params.get('puntos_minimos', 0))
        donaciones_minimas = int(request.query_params.get('donaciones_minimas', 0))
        max_colaboradores = int(request.query_params.get('max_colaboradores', 10))

        ultimo_mes = timezone.now() - timedelta(days=30)

        colaboradores = Colaborador.objects.annotate(
            total_donaciones=models.Sum(
                models.Case(
                    models.When(donaciones__fecha__gte=ultimo_mes, then='donaciones__cantidad'),
                    default=0,
                    output_field=models.IntegerField(),
                )
            )
        ).filter(
            puntaje__gte=puntos_minimos,
            total_donaciones__gte=donaciones_minimas,
        ).order_by('-puntaje')[:max_colaboradores]

        serializer = ColaboradorSerializer(colaboradores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
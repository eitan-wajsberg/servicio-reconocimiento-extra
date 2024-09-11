import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reconocimientos_extra.settings')
django.setup()

from recomendar_colaboradores_app.models import Colaborador
from recomendar_colaboradores_app.serializers import ColaboradorSerializer
from recomendar_colaboradores_app.views import RecomendarColaboradoresAPIView

import json
from rest_framework.response import Response
from rest_framework import status

# Cadena JSON
json_str = '[{"tipo_documento": "DNI", "nro_documento": "12345678", "direccion": "Calle Falsa 123", "nombre": "Juan", "apellido": "Pérez", "fecha_nacimiento": "1985-06-15", "whatsapp": "+5491112345678", "mail": "juan.perez@example.com", "user_telegram": "@juanperez", "puntaje_neto": 120.50, "cantidad_viandas_ultimo_mes": 15}, {"tipo_documento": "DNI", "nro_documento": "87654321", "direccion": "Avenida Siempre Viva 742", "nombre": "Ana", "apellido": "García", "fecha_nacimiento": "1990-08-22", "whatsapp": "+5491123456789", "mail": "ana.garcia@example.com", "user_telegram": "@anagarcia", "puntaje_neto": 95.75, "cantidad_viandas_ultimo_mes": 10}, {"tipo_documento": "DNI", "nro_documento": "13579246", "direccion": "Calle Real 456", "nombre": "Luis", "apellido": "Martínez", "fecha_nacimiento": "1982-11-30", "whatsapp": "+5491134567890", "mail": "luis.martinez@example.com", "user_telegram": "@luismartinez", "puntaje_neto": 85.00, "cantidad_viandas_ultimo_mes": 20}]'

data = [
    {
        "tipo_documento": "DNI",
        "nro_documento": "12345678",
        "direccion": "Calle Falsa 123",
        "nombre": "Juan",
        "apellido": "Pérez",
        "fecha_nacimiento": "1985-06-15",
        "whatsapp": "+5491112345678",
        "mail": "juan.perez@example.com",
        "user_telegram": "@juanperez",
        "puntaje_neto": 120.50,
        "cantidad_viandas_ultimo_mes": 15
    },
    {
        "tipo_documento": "DNI",
        "nro_documento": "87654321",
        "direccion": "Avenida Siempre Viva 742",
        "nombre": "Ana",
        "apellido": "García",
        "fecha_nacimiento": "1990-08-22",
        "whatsapp": "+5491123456789",
        "mail": "ana.garcia@example.com",
        "user_telegram": "@anagarcia",
        "puntaje_neto": 95.75,
        "cantidad_viandas_ultimo_mes": 10
    },
    {
        "tipo_documento": "DNI",
        "nro_documento": "13579246",
        "direccion": "Calle Real 456",
        "nombre": "Luis",
        "apellido": "Martínez",
        "fecha_nacimiento": "1982-11-30",
        "whatsapp": "+5491134567890",
        "mail": "luis.martinez@example.com",
        "user_telegram": "@luismartinez",
        "puntaje_neto": 85.00,
        "cantidad_viandas_ultimo_mes": 20
    }
]

# Convertir JSON a diccionario
diccionario = json.loads(json_str)

# Crear el serializador con many=True para una lista de objetos
serializer = ColaboradorSerializer(data=diccionario, many=True)

RecomendarColaboradoresAPIView.post(RecomendarColaboradoresAPIView, json_str)

"""# Validar y guardar los datos
if serializer.is_valid():
    serializer.save()
    print("Data saved successfully")
else:
    print("Errors:", serializer.errors)"""

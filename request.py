import requests
from requests.auth import HTTPBasicAuth
url = 'http://localhost:8000/recomendar-colaboradores/'
data = {
    "puntos_minimos": 50,
    "donaciones_minimas": 10,
    "max_colaboradores": 5,
    "colaboradores": [
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
            "direccion": "Avenida Siempreviva 742",
            "nombre": "María",
            "apellido": "García",
            "fecha_nacimiento": "1990-08-20",
            "whatsapp": "+5491123456789",
            "mail": "maria.garcia@example.com",
            "user_telegram": "@mariagarcia",
            "puntaje_neto": 95.75,
            "cantidad_viandas_ultimo_mes": 20
        },
        {
            "tipo_documento": "DNI",
            "nro_documento": "11223344",
            "direccion": "Pasaje Sin Nombre 456",
            "nombre": "Carlos",
            "apellido": "López",
            "fecha_nacimiento": "1978-03-10",
            "whatsapp": "+5491134567890",
            "mail": "carlos.lopez@example.com",
            "user_telegram": "@carloslopez",
            "puntaje_neto": 80.00,
            "cantidad_viandas_ultimo_mes": 12
        }
    ]
}

data = {
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
}

payload = { 
    "colaboradores": [
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
        "direccion": "Avenida Siempreviva 742",
        "nombre": "María",
        "apellido": "García",
        "fecha_nacimiento": "1990-08-20",
        "whatsapp": "+5491123456789",
        "mail": "maria.garcia@example.com",
        "user_telegram": "@mariagarcia",
        "puntaje_neto": 95.75,
        "cantidad_viandas_ultimo_mes": 20
    },
    {
        "tipo_documento": "DNI",
        "nro_documento": "11223344",
        "direccion": "Pasaje Sin Nombre 456",
        "nombre": "Carlos",
        "apellido": "López",
        "fecha_nacimiento": "1978-03-10",
        "whatsapp": "+5491134567890",
        "mail": "carlos.lopez@example.com",
        "user_telegram": "@carloslopez",
        "puntaje_neto": 80.00,
        "cantidad_viandas_ultimo_mes": 12
    }
    # Agrega más colaboradores si es necesario
] }

import requests
from requests.auth import HTTPBasicAuth
import json

import requests
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:8000/recomendar-colaboradores/"
data = {
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
}

username = "admin"
password = "123456"

response = requests.post(
    url,
    json=data,  # Enviar datos JSON
    auth=HTTPBasicAuth(username, password)  # Autenticación básica
)

print("Status Code:", response.status_code)
print("Response Text:", response.text)

"""auth=HTTPBasicAuth(username, password)
#response = requests.get(url, json=data)
response = requests.get(url, auth=HTTPBasicAuth(username, password), json=data)
print(response.status_code)
print(response.text)
try:
    data = response.json()
except requests.exceptions.JSONDecodeError:
    print("La respuesta no contiene un JSON válido.")
    data = None
"""
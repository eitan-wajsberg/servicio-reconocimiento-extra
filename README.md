# Servicio de reconocimiento extra
Servicio realizado para el trabajo práctico anual correspondiente a la asignatura Diseño de Sistemas de la carrera de Ingeniería en Sistemas de Información de la Universidad Tecnológica Nacional FRBA. 

## Integrantes del grupo
- Facundo Gauna Somá
- Nehuen Balian Amaros
- Rocio Ochoa Charlín
- Marco Bravo
- Eitan Wajsberg

## Descripción y contexto del servicio
Hay empresas que decidieron brindar beneficios a los colaboradores pero desde sus propias plataformas. Para eso vamos a implementar un servicio que recomiende colaboradores de acuerdo a los parámetros solicitados por las distintas empresas.
La empresa solicitará una cantidad mínima de puntos requeridos, una cantidad mínima de donación de viandas realizada en el último mes y una cantidad máxima de colaboradores a ser incorporados en la plataforma externa. En caso de que no se llegue a la cantidad de colaboradores solicitados, se deberán devolver únicamente los que cumplan las condiciones.
Nuestro sistema debe devolver una lista de colaboradores a ser reconocidos por otras empresas, junto con el puntaje que obtuvo cada uno hasta el momento.

## Tecnología y lenguaje elegido
Decidimos utilizar como lenguaje Python y Django tanto como ORM como para hacer la API REST. 
Django utiliza el Active Record pattern para su ORM. En este patrón, cada modelo en Django representa tanto la estructura de la tabla en la base de datos como las operaciones que se pueden realizar en esa tabla. Es decir, las instancias de los modelos en Django son responsables de contener sus datos y los métodos para interactuar con la base de datos.
Esto significa que las instancias de un modelo en Django no solo representan una fila en la base de datos, sino que también tienen métodos para guardar, actualizar, eliminar, y realizar otras operaciones directamente desde esa instancia, que es una característica clave del patrón Active Record.

# Guía de Uso en Local

Esta guía detalla los pasos para configurar y ejecutar el servicio de reconocimiento extra en un entorno local utilizando Django.

## Requisitos Previos

### Instalación de Dependencias

Antes de comenzar, asegúrate de tener instalado lo siguiente:

1. **Python 3.10 o superior**: Puedes descargar Python desde [aquí](https://www.python.org/downloads/).
2. **MySQL**: Asegúrate de tener instalado y configurado MySQL. Puedes descargar MySQL desde [aquí](https://dev.mysql.com/downloads/installer/).

### Instalar Django y otras Dependencias

Instala Django y las demás dependencias del proyecto utilizando `pip`:

```bash
pip install Django==5.1.1 mysqlclient
```

> **Nota:** `mysqlclient` es necesario para conectar Django con MySQL.

## Configuración de la Base de Datos

Abre el archivo `reconocimientos_extra/settings.py` y localiza la configuración de la base de datos. Debes modificar los parámetros para que coincidan con tu configuración local de MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'servicio-reconocimientos-extra',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

- **NAME**: Nombre de la base de datos que crearás para el proyecto.
- **USER**: Usuario de la base de datos con permisos para crear y modificar tablas.
- **PASSWORD**: Contraseña del usuario de la base de datos.
- **HOST**: Dirección del servidor de base de datos (usualmente `localhost` para entornos locales).
- **PORT**: Puerto por defecto de MySQL (`3306`).

### Creación de la Base de Datos

Accede a MySQL desde la terminal o desde una herramienta gráfica (como MySQL Workbench) y crea la base de datos que usará Django:

```sql
CREATE DATABASE servicio-reconocimientos-extra CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Migraciones y Configuración Inicial

1. **Aplicar Migraciones**: Ejecuta las migraciones para crear las tablas necesarias en la base de datos:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. **Crear Superusuario**: Esto te permitirá acceder al panel de administración de Django. Ejecuta el siguiente comando y sigue las instrucciones para definir el nombre de usuario, correo y contraseña:

    ```bash
    python manage.py createsuperuser
    ```

3. **Iniciar el Servidor de Desarrollo**: Una vez configurada la base de datos y creado el superusuario, puedes iniciar el servidor local:

    ```bash
    python manage.py runserver
    ```

    El servidor estará disponible en `http://127.0.0.1:8000/` por defecto.

## Acceso al Panel de Administración

Para acceder al panel de administración de Django, donde puedes gestionar los modelos y la base de datos, navega a:

```
http://127.0.0.1:8000/admin/
```

Inicia sesión con las credenciales del superusuario que creaste anteriormente.

# Documentación de la API - RecomendarColaboradoresAPIView

## Descripción

Esta API recomienda colaboradores basados en los parámetros proporcionados y crea registros de solicitud, solicitante y recomendación.

## Método

`POST`

## URL

`/recomendar-colaboradores/`

## Parámetros de Solicitud

**Cuerpo de la solicitud (`request body`):**

```json
{
    "puntos_minimos": 50,
    "donaciones_minimas": 5,
    "max_colaboradores": 10,
    "solicitante": {
        "razon_social": "Empresa U",
        "rubro": "Tecnología",
        "whatsapp": "+1234567890",
        "mail": "contacto@empresa.com",
        "user_telegram": "@empresa999",
        "direccion": "123 Calle Falsa"
    },
    "colaboradores": [
        {
            "tipo_documento": "DNI",
            "nro_documento": "87654321",
            "direccion": "789 Calle Nueva",
            "nombre": "Ana",
            "apellido": "Gómez",
            "fecha_nacimiento": "1990-05-15",
            "whatsapp": "+1122334455",
            "mail": "ana@ejemplo.com",
            "user_telegram": "@ana",
            "puntaje_neto": 70,
            "cantidad_viandas_ultimo_mes": 15
        }
        // más colaboradores...
    ]
}
```

## Respuesta Exitosa

**Código de Estado:** 200 OK
**Cuerpo de la respuesta (response body):**
```json
{
    "message": "Solicitud, Solicitante, y Recomendación guardados exitosamente.",
    "data": {
        "solicitante": {
            "id": 1,
            "razon_social": "Empresa U",
            "rubro": "Tecnología",
            "whatsapp": "+1234567890",
            "mail": "contacto@empresa.com",
            "user_telegram": "@empresa999",
            "direccion": "123 Calle Falsa"
        },
        "solicitud": {
            "id": 1,
            "cant_min_puntos": 50,
            "cant_min_viandas_ultimo_mes": 5,
            "fecha": "2024-09-11",
            "cant_max_colaboradores": 10,
            "solicitante": 1
        },
        "colaboradores": [
            {
                "id": 1,
                "tipo_documento": "DNI",
                "nro_documento": "87654321",
                "direccion": "789 Calle Nueva",
                "nombre": "Ana",
                "apellido": "Gómez",
                "fecha_nacimiento": "1990-05-15",
                "whatsapp": "+1122334455",
                "mail": "ana@ejemplo.com",
                "user_telegram": "@ana",
                "puntaje_neto": 70,
                "cantidad_viandas_ultimo_mes": 15
            }
            // más colaboradores...
        ],
        "recomendacion": {
            "id": 1,
            "fecha_recomendacion": "2024-09-11"
        }
    }
}
```

## Respuestas de Error

**Código de Estado:** 400 Bad Request.

**Ejemplos de cuerpo de respuesta (response body):**

```json
{
    "error": "El campo 'solicitante' debe ser un diccionario."
}
```
```json
{
    "error": "No se encontraron colaboradores con los criterios especificados."
}
```
```json
{
    "error": "Este campo no puede ser nulo."
}
```
```json
{
    "error": "Error al procesar los datos del colaborador.",
    "details": {
        "colaboradores": [
            "Field 'id' expected a number but got {'tipo_documento': 'DNI', ...}"
        ]
    }
}
```

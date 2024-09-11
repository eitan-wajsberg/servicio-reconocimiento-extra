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

# Documentación de la API

## Endpoint: Recomendar Colaboradores

**Método:** `GET`

**URL:** `/recomendar-colaboradores/`

**Descripción:**
Obtiene una lista de colaboradores recomendados basados en los parámetros de puntuación mínima y donaciones mínimas.

**Parámetros de Consulta:**

- `puntos_minimos` (opcional): La puntuación mínima requerida para los colaboradores. Tipo: `integer`. Valor predeterminado: `0`.
- `donaciones_minimas` (opcional): La cantidad mínima de viandas donadas en el último mes. Tipo: `integer`. Valor predeterminado: `0`.
- `max_colaboradores` (opcional): El número máximo de colaboradores a devolver. Tipo: `integer`. Valor predeterminado: `10`.

**Ejemplo de Solicitud:**

```http
GET /recomendar-colaboradores/?puntos_minimos=50&donaciones_minimas=5&max_colaboradores=3 HTTP/1.1
Host: localhost:8000
```

## Cargar Colaboradores

**Método:** `POST`

**URL:** `/recomendar-colaboradores/`

**Descripción:**
Permite cargar una lista de colaboradores a la base de datos.

**Cuerpo de la Solicitud:**

- Tipo: application/json
- Contenido: Una lista de objetos de colaborador.

**Ejemplo de Solicitud:**

```http
POST /carga-colaboradores/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json

[
    {
        "tipo_documento": "DNI",
        "nro_documento": "12345678",
        "direccion": "Calle Falsa 123",
        "nombre": "Juan",
        "apellido": "Pérez",
        "fecha_nacimiento": "1980-01-01",
        "whatsapp": "+123456789",
        "mail": "juan.perez@example.com",
        "user_telegram": "@juanperez",
        "puntaje_neto": "75.50",
        "cantidad_viandas_ultimo_mes": 10
    },
    {
        "tipo_documento": "DNI",
        "nro_documento": "87654321",
        "direccion": "Avenida Siempre Viva 742",
        "nombre": "Ana",
        "apellido": "Gómez",
        "fecha_nacimiento": "1990-05-15",
        "whatsapp": "+987654321",
        "mail": "ana.gomez@example.com",
        "user_telegram": "@anagomez",
        "puntaje_neto": "80.00",
        "cantidad_viandas_ultimo_mes": 5
    }
]
```
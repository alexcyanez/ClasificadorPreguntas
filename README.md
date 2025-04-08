# App Clasificadora de preguntas usando LLM de OPENAI

La app utiliza **FastAPI** y la **API de OpenAI**  para clasificar preguntas en distintas categorías (legal, contable, médica) y responderlas con un estilo especializado para cada rubro.

## Características y requisitos

- Clasificación automática de preguntas usando la API de OpenAI (modelo 4o-mini)
- Docker-ready para despliegue rápido.
- Configuración flexible con variables de entorno (`.env`).

- Python 3.11
- OpenAI API Key
- Docker (aunque puede ser opcional)

## Estructura del proyecto:


```bash
├── ClasificadorPreguntas/ 
  ├── app.py
  ├── utils.py
  ├── test.py
  ├── requirements.txt
  ├── Dockerfile
  ├── docker-compose.yml
  ├── README.md
```


## Instalación

Descarga el paquete y dentro de la carpeta donde tienes los archivos clonados genera tu .env con
tu api key para openai con la siguiente estructura: 
- OPENAI_API_KEY=tu-clave-de-openai


### Para correr con Docker:

- En el directorio del proyecto:

```bash
docker compose build
```
- Una vez que termine el proceso de instalación puedes correr la imagen:

```bash
docker run --env-file .env -p 8000:8000 image-clasificador
```
- puedes abrir el servidor en:

```bash
localhost:8000
```

## Uso

### Endpoint

- Para hacer una consulta debes hacer un post a:
```bash
localhost:8000/preguntar
```
- Aquí un ejemplo usando
```bash
curl
```

```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/preguntar' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "pregunta": "¿Cómo debo llevar la contabilidad de mi empresa?"
}'
```

- Respuesta del ejemplo:

```bash
{
  "categoria": "contable",
  "respuesta": "Para llevar la contabilidad de tu empresa de manera efectiva, sigue estos pasos básicos:\n\n1. **Elige un método contable**: Puedes optar por el método de caja (registras ingresos y gastos cuando realmente ocurren) o el método de acumulación (registras cuando se generan las transacciones, independientemente de cuándo se realicen los pagos).\n\n2. **Organiza tus documentos**: Mantén todos tus recibos, facturas y comprobantes en orden. Puedes usar carpetas físicas o herramientas digitales para almacenarlos.\n\n3. **Registra tus transacciones**: Lleva un registro diario de todas las entradas y salidas de dinero. Esto incluye ventas, compras, gastos y cualquier otro movimiento financiero.\n\n4. **Utiliza software contable**: Considera usar un programa de contabilidad que te ayude a automatizar procesos, como QuickBooks o Xero. Esto hará que sea más fácil llevar un control y generar informes.\n\n5. **Revisa tus finanzas regularmente**: Haz un balance mensual o trimestral para entender cómo está funcionando tu negocio. Esto te ayudará a tomar decisiones informadas.\n\n6. **Consulta a un profesional**: Si no te sientes seguro, considera contratar a un contador o asesor financiero que te guíe en el proceso y te ayude con los aspectos más complejos.\n\nSiguiendo estos pasos, podrás llevar la contabilidad de tu empresa de manera más organizada y efectiva."
}
```

### Ejemplo del manejo de preguntas fuera de los tres rubros o categorias:

- POST:
```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/preguntar' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "pregunta": "¿Qué equipo ganó la copa mundial de football en 2010?"
}'
```
- Respuesta:
```bash
{
  "detail": "La pregunta no está dentro de las categorias, por favor intente con otra pregunta"
}
``` 

## License

[MIT](https://choosealicense.com/licenses/mit/)

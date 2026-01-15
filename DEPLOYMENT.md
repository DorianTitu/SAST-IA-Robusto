# 🚀 Railway Deployment Guide

## ✅ Pre-requisitos

- Cuenta en [Railway.app](https://railway.app)
- GitHub conectado a Railway
- Google Gemini API Key

## 📋 Pasos para Deploy en Railway

### 1️⃣ Conectar el Repositorio

1. Ve a [railway.app](https://railway.app)
2. Crea un nuevo proyecto → "Deploy from GitHub"
3. Selecciona tu repositorio `SAST-IA-Robusto`
4. Railway detectará automáticamente el Dockerfile

### 2️⃣ Configurar Variables de Entorno

En el dashboard de Railway, en la sección "Variables":

```env
GEMINI_API_KEY=tu_api_key_aqui
ENVIRONMENT=production
PYTHONUNBUFFERED=1
```

Railway expone automáticamente `$PORT` como variable de entorno.

### 3️⃣ Configuración de Build

Railway buscará en este orden:
- ✅ `Dockerfile` (lo tenemos)
- ✅ `railway.json` (lo tenemos)
- ✅ `docker-compose.yml` (soportado)

### 4️⃣ Puerto

- **Puerto interno**: 8000 (definido en `EXPOSE 8000`)
- **Puerto público**: Asignado automáticamente por Railway
- **Variable de entorno**: `$PORT` (si necesitas cambiar)

Railway mapeará automáticamente el puerto 8000.

## 🏗️ Estructura para Railway

```
SAST-IA-Robusto/
├── Dockerfile               ✅ (ubicación: docker/Dockerfile)
├── requirements.txt         ✅ 
├── railway.json            ✅ (opcional pero recomendado)
├── .dockerignore           ✅
├── src/artheon_sast/       ✅
├── docker/                 ✅
└── .env.example            ✅
```

## ✨ Características Habilitadas para Railway

✅ **Healthcheck**: Endpoint `/health` monitorea la salud de la app
✅ **Workers**: Configurado para 1 worker (ajustable)
✅ **Port Binding**: `0.0.0.0:8000` (escucha en todas las interfaces)
✅ **Environment Variables**: Soporte completo
✅ **Logging**: Output de uvicorn visible en logs
✅ **Auto-restart**: Railway reinicia si falla

## 🔐 Manejo de Secretos

### ⚠️ IMPORTANTE: API Key

**NUNCA** commites tu `.env` con la API key real.

Usa `.env.example` como referencia:
```bash
cp .env.example .env
# Edita .env locally
```

En Railway, agrega la variable en el dashboard, no en el código.

## 📊 Monitoreo

### Logs en Railway

Railway automáticamente captura:
```
✅ uvicorn startup logs
✅ API requests/responses
✅ Errores y excepciones
✅ Healthcheck pings
```

### Endpoint de Salud

```bash
curl https://your-app.railway.app/health
```

## 🧪 Probar Localmente Antes de Deploy

```bash
# Build como lo haría Railway
docker build -f docker/Dockerfile -t artheon-sast .

# Run
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=tu_key \
  -e ENVIRONMENT=production \
  artheon-sast
```

## 🌐 URLs Públicas

Una vez deployado, Railway te proporciona una URL como:
```
https://artheon-sast-xxx.railway.app
```

### Endpoints disponibles:

```
GET  https://artheon-sast-xxx.railway.app/health
GET  https://artheon-sast-xxx.railway.app/docs
GET  https://artheon-sast-xxx.railway.app/redoc

POST https://artheon-sast-xxx.railway.app/api/v1/analyze
POST https://artheon-sast-xxx.railway.app/api/v1/analyze-files
```

## 🆘 Troubleshooting

### ❌ "Port already in use"
Railway asigna el puerto automáticamente. Este error no debería ocurrir.

### ❌ "Module not found"
- Verifica que `requirements.txt` tenga todas las dependencias
- El Dockerfile instala dependencias antes de copiar código

### ❌ "Healthcheck failing"
- Verifica que `/health` endpoint esté disponible
- Railway espera 5 segundos antes de empezar healthchecks

### ❌ "API Key not working"
- Verifica que `GEMINI_API_KEY` esté en las variables de Railway
- No debería estar en el archivo `.env` commiteado

## 📈 Escalabilidad

Para escalar en Railway:
1. Aumenta **numReplicas** en `railway.json`
2. Railway balanceará automáticamente el tráfico
3. Cada réplica corre independientemente

## 🔄 Actualizaciones

Cada commit a `main`:
1. GitHub notifica a Railway
2. Railway rebuild la imagen Docker
3. Redeploy automático
4. Sin downtime (con múltiples replicas)

## 📚 Recursos

- [Railway Docs](https://docs.railway.app)
- [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)

---

**¡Listo para Railway!** 🚀

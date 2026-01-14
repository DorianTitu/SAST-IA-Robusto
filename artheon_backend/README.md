# 🛡️ ARTHEON-SAST Backend

Backend FastAPI para análisis estático de seguridad (SAST). Detecta vulnerabilidades en código fuente.

## 🚀 Inicio Rápido con Docker

### Opción 1: Docker Compose (Recomendado)

```bash
cd artheon_backend
docker-compose up --build
```

La aplicación estará disponible en: **http://localhost:8000**

### Opción 2: Docker Manual

```bash
cd artheon_backend

# Construir imagen
docker build -t artheon-sast-backend:latest .

# Ejecutar contenedor
docker run -p 8000:8000 -v /:/host:ro artheon-sast-backend:latest
```

### Opción 3: Ejecución Local (sin Docker)

```bash
cd artheon_backend

# Crear virtual environment
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📡 API Endpoints

### 1. Health Check

```bash
curl http://localhost:8000/health
```

**Respuesta:**
```json
{
    "status": "healthy",
    "service": "ARTHEON-SAST Backend"
}
```

### 2. Analizar Directorio

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"directory": "/path/to/project"}'
```

**Respuesta Ejemplo:**
```json
{
    "directory": "/Users/user/mi-proyecto",
    "languages_detected": ["javascript", "python"],
    "language_details": {
        "javascript": {
            "files": 15,
            "extensions": [".js", ".ts"]
        },
        "python": {
            "files": 8,
            "extensions": [".py"]
        }
    },
    "total_files": 23,
    "supported": true
}
```

### 3. Listar Archivos por Lenguaje

```bash
curl -X POST http://localhost:8000/analyze-files \
  -H "Content-Type: application/json" \
  -d '{"directory": "/path/to/project"}'
```

**Respuesta:**
```json
{
    "directory": "/Users/user/mi-proyecto",
    "files_by_language": {
        "javascript": [
            "/Users/user/mi-proyecto/src/app.js",
            "/Users/user/mi-proyecto/src/main.ts"
        ],
        "python": [
            "/Users/user/mi-proyecto/scripts/setup.py"
        ]
    }
}
```

## 📚 Documentación Interactiva

Una vez que el servidor está corriendo, accede a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔍 Lenguajes Soportados

| Lenguaje | Extensiones |
|----------|-----------|
| **JavaScript** | `.js`, `.jsx`, `.ts`, `.tsx`, `.mjs`, `.cjs` |
| **Python** | `.py`, `.pyw`, `.pyi` |
| **PHP** | `.php`, `.php3`, `.php4`, `.php5`, `.php7`, `.php8`, `.phtml`, `.phps` |
| **Java** | `.java` |

## 🛠️ Estructura del Proyecto

```
artheon_backend/
├── main.py                  # Aplicación FastAPI
├── language_analyzer.py     # Módulo de análisis de lenguajes
├── requirements.txt         # Dependencias Python
├── Dockerfile              # Configuración Docker
├── docker-compose.yml      # Composición de servicios
├── .dockerignore           # Archivos a ignorar en imagen
└── README.md               # Este archivo
```

## 🐳 Comandos Docker Útiles

```bash
# Ver logs del contenedor
docker logs artheon-sast-backend

# Conectar a bash del contenedor
docker exec -it artheon-sast-backend /bin/bash

# Detener contenedor
docker stop artheon-sast-backend

# Iniciar contenedor detenido
docker start artheon-sast-backend

# Remover contenedor
docker rm artheon-sast-backend
```

## 🔧 Variables de Entorno

Actualmente no se requieren variables de entorno específicas. En futuras versiones:

```bash
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net
DEBUG=True
```

## ⚡ Próximos Pasos

1. **Integración de Análisis SAST completo**
2. **Integración con Google API para recomendaciones**
3. **Persistencia en MongoDB**
4. **Análisis de vulnerabilidades en tiempo real**
5. **Generación de reportes HTML**

## 📝 Ejemplo de Uso Completo

```python
import requests

API_URL = "http://localhost:8000"

# Analizar directorio
response = requests.post(
    f"{API_URL}/analyze",
    json={"directory": "/Users/user/mi-proyecto"}
)

if response.status_code == 200:
    result = response.json()
    print(f"Lenguajes detectados: {result['languages_detected']}")
    print(f"Total de archivos: {result['total_files']}")
else:
    print(f"Error: {response.status_code}")
```

## 📄 Licencia

MIT

## 👤 Autor

ARTHEON-SAST Project - 2026

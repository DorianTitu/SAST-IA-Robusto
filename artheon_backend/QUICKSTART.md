# 🚀 ARTHEON-SAST Backend - Guía de Uso

## ✅ Estado Actual

✔️ **API FastAPI funcionando correctamente en Docker**  
✔️ **Análisis de lenguajes: JavaScript, Python, PHP, Java**  
✔️ **2 endpoints principales operativos**  

## 📍 Acceso al API

- **URL Base:** `http://localhost:8000`
- **Documentación Swagger:** `http://localhost:8000/docs`
- **Documentación ReDoc:** `http://localhost:8000/redoc`

## 🐳 Comandos Docker Útiles

### Iniciar el backend
```bash
cd /Users/doriantituana/Desktop/Dorian/Tesis/SAST-rOBUSTO/artheon_backend
docker-compose up -d
```

### Ver logs
```bash
docker logs artheon-sast-backend -f
```

### Detener el backend
```bash
docker stop artheon-sast-backend
```

### Reiniciar el backend
```bash
docker-compose restart
```

## 📡 Endpoints Disponibles

### 1. **Health Check**
```bash
curl http://localhost:8000/health
```

### 2. **Analizar Directorio** (Detectar Lenguajes)
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "directory": "/ruta/al/proyecto"
  }'
```

**Respuesta Ejemplo:**
```json
{
    "directory": "/app/test_project",
    "languages_detected": ["java", "javascript", "php", "python"],
    "language_details": {
        "javascript": {
            "files": 2,
            "extensions": [".js", ".ts"]
        },
        "python": {
            "files": 1,
            "extensions": [".py"]
        },
        "php": {
            "files": 1,
            "extensions": [".php"]
        },
        "java": {
            "files": 1,
            "extensions": [".java"]
        }
    },
    "total_files": 5,
    "supported": true
}
```

### 3. **Listar Archivos por Lenguaje**
```bash
curl -X POST http://localhost:8000/analyze-files \
  -H "Content-Type: application/json" \
  -d '{
    "directory": "/ruta/al/proyecto"
  }'
```

**Respuesta Ejemplo:**
```json
{
    "directory": "/app/test_project",
    "files_by_language": {
        "javascript": [
            "/app/test_project/src/app.js",
            "/app/test_project/src/main.ts"
        ],
        "python": [
            "/app/test_project/scripts/setup.py"
        ],
        "php": [
            "/app/test_project/index.php"
        ],
        "java": [
            "/app/test_project/Main.java"
        ]
    }
}
```

## 🎯 Próximos Pasos

1. **Integración SAST Completa**
   - [ ] Cargar reglas de vulnerabilidades
   - [ ] Escaneo con patrones regex
   - [ ] Endpoint `/scan` para análisis completo

2. **Integración Google Gemini API**
   - [ ] Obtener recomendaciones de correcciones
   - [ ] Endpoint `/recommendations`
   - [ ] Generación de soluciones automáticas

3. **Persistencia de Datos**
   - [ ] MongoDB para histórico
   - [ ] Almacenamiento de reportes
   - [ ] Estadísticas de tendencias

4. **Reportes HTML**
   - [ ] Endpoint `/report` 
   - [ ] Generación de reportes interactivos
   - [ ] Exportación a PDF

## 📝 Ejemplo de Uso Completo (Python)

```python
import requests
import json

API_URL = "http://localhost:8000"

# Paso 1: Analizar directorio
response = requests.post(
    f"{API_URL}/analyze",
    json={"directory": "/ruta/proyecto"}
)

if response.status_code == 200:
    analysis = response.json()
    print("🔍 Lenguajes detectados:")
    for lang, details in analysis['language_details'].items():
        print(f"  • {lang}: {details['files']} archivos")
    
    # Paso 2: Obtener archivos por lenguaje
    response = requests.post(
        f"{API_URL}/analyze-files",
        json={"directory": "/ruta/proyecto"}
    )
    
    files = response.json()['files_by_language']
    print("\n📄 Archivos encontrados:")
    for lang, file_list in files.items():
        print(f"  {lang}:")
        for file in file_list:
            print(f"    - {file}")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.json())
```

## 🔧 Estructura del Proyecto

```
artheon_backend/
├── main.py                      # App FastAPI
├── language_analyzer.py         # Módulo de análisis
├── requirements.txt             # Dependencias
├── Dockerfile                   # Configuración Docker
├── docker-compose.yml           # Composición
├── .dockerignore               # Archivos ignorados
├── README.md                    # Documentación general
└── QUICKSTART.md                # Esta guía
```

## 🆘 Solución de Problemas

### El contenedor no inicia
```bash
# Ver logs
docker logs artheon-sast-backend

# Rebuild
docker-compose down
docker-compose up --build
```

### Puerto 8000 ya está en uso
```bash
# Cambiar puerto en docker-compose.yml
# Editar: ports: ["8001:8000"]
```

### No encuentra directorio
- Asegúrate de usar rutas absolutas dentro del contenedor
- Los directorios del host están en `/host` (montado como read-only)
- Para tu Mac, usa: `/host/Users/...`

---

**Backend ARTHEON-SAST listo para integración de análisis SAST + Google Gemini API** 🛡️

# 🛡️ ARTHEON-SAST: Static Application Security Testing

Sistema robusto de análisis estático de seguridad con integración de **Google Gemini API** para recomendaciones automáticas de correcciones.

## 📋 Contenido del Proyecto

```
SAST-rOBUSTO/
├── artheon_backend/              # Backend FastAPI con Docker
│   ├── main.py                   # Aplicación principal
│   ├── language_analyzer.py      # Análisis de lenguajes
│   ├── requirements.txt          # Dependencias Python
│   ├── Dockerfile                # Configuración Docker
│   ├── docker-compose.yml        # Composición de servicios
│   ├── README.md                 # Documentación del backend
│   └── QUICKSTART.md             # Guía rápida
├── IMPLEMENTATION_PLAN.md        # Plan de implementación
└── README.md                     # Este archivo

```

## 🚀 Quick Start

### Opción 1: Con Docker Compose (Recomendado)

```bash
cd artheon_backend
docker-compose up -d
```

Luego accede a:
- **API:** http://localhost:8000
- **Documentación:** http://localhost:8000/docs

### Opción 2: Local sin Docker

```bash
cd artheon_backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## 📡 API Endpoints

### 1. Health Check
```bash
curl http://localhost:8000/health
```

### 2. Detectar Lenguajes
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"directory": "/app/proyecto"}'
```

**Respuesta:**
```json
{
    "languages_detected": ["javascript", "python", "java", "php"],
    "language_details": {
        "javascript": {"files": 15, "extensions": [".js", ".ts"]},
        "python": {"files": 8, "extensions": [".py"]}
    },
    "total_files": 23,
    "supported": true
}
```

### 3. Listar Archivos
```bash
curl -X POST http://localhost:8000/analyze-files \
  -H "Content-Type: application/json" \
  -d '{"directory": "/app/proyecto"}'
```

## ✨ Características Actuales

✅ **FastAPI Backend en Docker**
- Servidor REST con documentación automática
- Validación de datos con Pydantic
- CORS habilitado

✅ **Análisis de Lenguajes**
- Detecta: JavaScript, Python, PHP, Java
- Mapeo automático de extensiones
- Ignorancia de directorios comunes (`node_modules`, `venv`, etc.)

✅ **Endpoints Funcionales**
- `/health` - Verificación de estado
- `/analyze` - Análisis de lenguajes en directorio
- `/analyze-files` - Listado de archivos por lenguaje

## 🔄 Próximas Fases

### FASE 2: Escaneo SAST Completo
- [ ] Cargar reglas de vulnerabilidades
- [ ] Escaneo con patrones regex
- [ ] Endpoint `/scan` completo
- [ ] Clasificación por severidad (Critical, High, Medium, Low)

### FASE 3: Integración Google Gemini
- [ ] Configuración de API Key
- [ ] Generación de recomendaciones automáticas
- [ ] Endpoint `/recommendations`
- [ ] Soluciones de código

### FASE 4: Persistencia (MongoDB)
- [ ] Almacenamiento de resultados
- [ ] Histórico de escaneos
- [ ] Estadísticas y tendencias

### FASE 5: Reportes HTML
- [ ] Generación de reportes interactivos
- [ ] Visualización de vulnerabilidades
- [ ] Exportación a múltiples formatos

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────┐
│  Cliente / CI-CD Pipeline                    │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│  FastAPI Backend (Port 8000)                │
│  ├─ /analyze (Detectar lenguajes)          │
│  ├─ /analyze-files (Listar archivos)       │
│  ├─ /scan (Análisis SAST completo)         │
│  └─ /recommendations (Google Gemini)       │
└────────────────┬────────────────────────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
┌──────────────┐   ┌──────────────────┐
│   Security   │   │  Google Gemini   │
│   Scanner    │   │  API             │
│   (SAST)     │   │  (Recomendaciones│
└──────────────┘   └──────────────────┘
        │
        ▼
┌──────────────────────────────────────────────┐
│  MongoDB (Opcional)                          │
│  - Histórico de escaneos                    │
│  - Estadísticas                             │
└──────────────────────────────────────────────┘
```

## 🐳 Comandos Docker Útiles

```bash
# Construir imagen
docker build -t artheon-sast:latest artheon_backend/

# Ejecutar con docker-compose
docker-compose -f artheon_backend/docker-compose.yml up -d

# Ver logs
docker logs artheon-sast-backend -f

# Conectar a contenedor
docker exec -it artheon-sast-backend bash

# Detener
docker stop artheon-sast-backend

# Remover
docker rm artheon-sast-backend
```

## 📊 Lenguajes Soportados

| Lenguaje | Extensiones | Estado |
|----------|-----------|--------|
| **JavaScript** | `.js`, `.jsx`, `.ts`, `.tsx`, `.mjs`, `.cjs` | ✅ Activo |
| **Python** | `.py`, `.pyw`, `.pyi` | ✅ Activo |
| **PHP** | `.php`, `.php3-8`, `.phtml` | ✅ Activo |
| **Java** | `.java` | ✅ Activo |
| **C/C++** | `.c`, `.cpp` | 🔄 Próximo |
| **Go** | `.go` | 🔄 Próximo |

## 🔐 Categorías de Vulnerabilidades (Futuro)

Cuando se implemente el SAST completo, detectará:

- 🔴 **CRITICAL**: eval(), SQL Injection, Command Injection
- 🟠 **HIGH**: XSS, Insecure Crypto, Path Traversal
- 🟡 **MEDIUM**: CORS Issues, No Input Validation
- 🟢 **LOW**: Code Quality, Deprecated APIs

## 📚 Documentación

- [Backend README](artheon_backend/README.md) - Documentación detallada del backend
- [Quick Start Guide](artheon_backend/QUICKSTART.md) - Guía rápida de uso
- [Implementation Plan](IMPLEMENTATION_PLAN.md) - Plan detallado de implementación

## 🛠️ Requisitos

- **Docker**: v20.10+
- **Python**: 3.8+ (si ejecutas local)
- **CPU**: Mínimo 2 núcleos
- **RAM**: Mínimo 2GB
- **Espacio Disco**: Mínimo 1GB

## 📦 Dependencias

```
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
python-multipart==0.0.6
```

En futuras fases se agregarán:
```
google-generativeai==0.3.0
pymongo==4.6.0
python-dotenv==1.0.0
```

## 🧪 Testing

```bash
cd artheon_backend

# Ejecutar tests
pytest tests/

# Coverage
pytest --cov=. tests/
```

## 📝 Ejemplos de Uso

### Python
```python
import requests

response = requests.post(
    "http://localhost:8000/analyze",
    json={"directory": "/app/proyecto"}
)

data = response.json()
print(f"Lenguajes: {data['languages_detected']}")
```

### JavaScript/Node.js
```javascript
const response = await fetch('http://localhost:8000/analyze', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({directory: '/app/proyecto'})
});

const data = await response.json();
console.log('Lenguajes:', data.languages_detected);
```

### cURL
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"directory": "/app/proyecto"}' | jq
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Ver [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Dorian Tituana** - ARTHEON-SAST Project  
2026 - Tesis de Seguridad de Software

## 📞 Soporte

- 📧 Email: [soporte]
- 🐛 Issues: GitHub Issues
- 💬 Discussiones: GitHub Discussions

---

## ✅ Estado del Proyecto

```
Fase 1: Backend Base           ✅ COMPLETO
Fase 2: SAST Completo         🔄 EN DESARROLLO
Fase 3: Google Gemini         ⏳ PRÓXIMO
Fase 4: MongoDB               ⏳ PRÓXIMO
Fase 5: Reportes HTML         ⏳ PRÓXIMO
```

## 🎯 Visión

Crear una herramienta SAST profesional, de código abierto y fácil de usar que:
- ✨ Detecte vulnerabilidades automáticamente
- 🤖 Genere soluciones con IA (Google Gemini)
- 📊 Produzca reportes visuales
- 🔄 Se integre fácilmente en pipelines CI/CD

---

**Última actualización:** 2026-01-14  
**Versión:** 1.0.0 (Beta)  
**Estado:** 🟢 En Desarrollo Activo

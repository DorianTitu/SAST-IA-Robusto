# ARTHEON SAST - Static Application Security Testing with Google Gemini

## Description

ARTHEON SAST is a Static Application Security Testing tool that uses Google Gemini API to automatically detect vulnerabilities in source code and provide security recommendations. This project analyzes multiple programming languages and integrates with AI models for intelligent vulnerability assessment.

## Supported Languages

- JavaScript/TypeScript (.js, .ts, .jsx, .tsx)
- Python (.py)
- PHP (.php)
- Java (.java)

## Requirements

- Python 3.8 or higher
- Docker and Docker Compose (for containerized deployment)
- Google Gemini API Key

## Installation

### Using Docker

```bash
cd docker
docker-compose up --build
```

The API will be available at http://localhost:8000

### Local Setup

```bash
git clone https://github.com/DorianTitu/SAST-IA-Robusto.git
cd SAST-IA-Robusto

python -m venv venv
source venv/bin/activate

pip install -e .

cp .env.example .env
# Add your GEMINI_API_KEY to .env

python -m uvicorn src.artheon_sast.api.main:app --reload
```

## API Endpoints

### Health Check
```
GET /health
```

### Analyze Directory
```
POST /api/v1/analyze
Content-Type: application/json

{
  "directory": "/path/to/analyze"
}
```

Response:
```json
{
  "directory": "/path/to/analyze",
  "languages_detected": ["javascript", "python", "java", "php"],
  "language_details": {
    "javascript": {"files": 5, "extensions": [".js", ".ts"]},
    "python": {"files": 3, "extensions": [".py"]},
    "java": {"files": 2, "extensions": [".java"]},
    "php": {"files": 0, "extensions": [".php"]}
  },
  "total_files": 10
}
```

### Analyze Files by Language
```
POST /api/v1/analyze-files
Content-Type: application/json

{
  "directory": "/path/to/analyze",
  "language": "javascript"
}
```

## Project Structure

```
src/artheon_sast/
├── api/                    API endpoints and routes
│   ├── main.py
│   └── routes.py
├── core/                   Domain logic
│   └── language_analyzer.py
├── services/               Business logic layer
│   └── language_service.py
├── models/                 Data validation schemas
│   └── schemas.py
├── rules/                  Security rules (future)
├── utils/                  Helper functions
└── config.py              Configuration settings
```

## Configuration

Configuration is centralized in `src/artheon_sast/config.py` and includes:
- Language file extensions mapping
- Directories to ignore during analysis
- Gemini model settings
- API configuration

Environment variables can be set via `.env` file.

## Documentation

- [Architecture Guide](docs/ARCHITECTURE.md) - System design and patterns
- [Quick Start Guide](docs/QUICKSTART.md) - Development workflow
- [Railway Deployment](RAILWAY_DEPLOYMENT.md) - Deployment instructions

Interactive API documentation available at http://localhost:8000/docs

## Testing

```bash
pytest
pytest --cov=src
pytest tests/test_language_analyzer.py
```

## Deployment

For Railway deployment, see [RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md)

## Author

Ismael Toala

## License

MIT License
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

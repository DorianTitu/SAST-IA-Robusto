# ARTHEON SAST - Static Application Security Testing with Google Gemini

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A robust Static Application Security Testing (SAST) tool powered by Google Gemini that automatically detects vulnerabilities and provides actionable security recommendations.

## 🎯 Features

- **Multi-Language Detection**: Automatically detects JavaScript, Python, PHP, and Java
- **Vulnerability Scanning**: Identifies security issues using pattern-based rules
- **AI-Powered Recommendations**: Leverages Google Gemini 2.0 Flash for intelligent recommendations
- **RESTful API**: Built with FastAPI for easy integration
- **Docker Support**: Container-ready deployment
- **Scalable Architecture**: Professional layered structure for easy extension

## 📋 Supported Languages

- **JavaScript/TypeScript** - Detects .js, .ts, .jsx, .tsx files
- **Python** - Detects .py files
- **PHP** - Detects .php files
- **Java** - Detects .java files

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose (recommended)
- OR Python 3.8+
- Google Gemini API Key

### Installation

#### Using Docker (Recommended)

```bash
cd docker
docker-compose up --build
```

The API will be available at `http://localhost:8000`

#### Local Installation

```bash
# Clone repository
git clone https://github.com/DorianTitu/SAST-IA-Robusto.git
cd SAST-IA-Robusto

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .

# Set up environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Run server
python -m uvicorn src.artheon_sast.api.main:app --reload
```

## 📡 API Endpoints

### Health Check
```bash
GET /health
```

### Analyze Directory
```bash
POST /api/v1/analyze
Content-Type: application/json

{
  "directory_path": "/path/to/analyze"
}
```

**Response**:
```json
{
  "directory": "/path/to/analyze",
  "languages_detected": {
    "javascript": 5,
    "python": 3,
    "java": 2,
    "php": 0
  },
  "total_files": 10,
  "analysis_timestamp": "2024-01-20T10:30:00Z"
}
```

### Analyze Files by Language
```bash
POST /api/v1/analyze-files
Content-Type: application/json

{
  "directory_path": "/path/to/analyze",
  "language": "javascript"
}
```

## 🏗️ Architecture

```
src/artheon_sast/
├── api/                    # FastAPI endpoints
│   ├── main.py
│   └── routes.py
├── core/                   # Core domain logic
│   └── language_analyzer.py
├── services/               # Business logic layer
│   └── language_service.py
├── models/                 # Pydantic schemas
│   └── schemas.py
├── rules/                  # Security rules (future)
├── utils/                  # Helper functions
└── config.py              # Centralized configuration
```

## 🔧 Configuration

Edit `src/artheon_sast/config.py` for:
- Language extensions
- Ignore directories
- Google Gemini model selection
- API settings

Or use environment variables via `.env` file.

## 📖 Documentation

- [Architecture Guide](docs/ARCHITECTURE.md) - Detailed system design
- [API Documentation](http://localhost:8000/docs) - Interactive Swagger UI (when running)
- [ReDoc Documentation](http://localhost:8000/redoc) - Alternative API docs

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test
pytest tests/test_language_analyzer.py
```

## 📦 Installation from PyPI (Future)

```bash
pip install artheon-sast
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Roadmap

### Phase 2: Enhanced SAST
- [ ] Complete vulnerability rule sets for all languages
- [ ] Security pattern database
- [ ] Severity classification

### Phase 3: Gemini Integration
- [ ] Automatic vulnerability recommendations
- [ ] Code review suggestions
- [ ] Risk assessment

### Phase 4: Persistence
- [ ] MongoDB integration
- [ ] Historical scanning
- [ ] Trend analysis

### Phase 5: Reporting
- [ ] HTML report generation
- [ ] PDF exports
- [ ] Executive summaries

## 🔐 Security Notes

- Never commit `.env` file with real API keys
- Use `.env.example` as template
- Rotate API keys regularly
- Store API keys in secure environment variable management system

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ✨ Acknowledgments

- Google Gemini API for AI-powered security recommendations
- FastAPI framework for building robust APIs
- Docker for containerization support

## 👨‍💻 Author

Dorian Tituana  
[GitHub](https://github.com/DorianTitu) | [Email](mailto:dorian.tituana@epn.edu.ec)

## 📧 Support

For issues, questions, or suggestions:
- Open an issue on [GitHub Issues](https://github.com/DorianTitu/SAST-IA-Robusto/issues)
- Check existing [documentation](docs/)

## ✨ Próximas Fases

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

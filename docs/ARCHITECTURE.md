# 🏗️ Arquitectura de ARTHEON-SAST

## Estructura del Proyecto

```
SAST-rOBUSTO/
├── src/                          # 📦 Código fuente
│   └── artheon_sast/             # Paquete principal
│       ├── __init__.py           # Inicializador
│       ├── config.py             # Configuración centralizada
│       │
│       ├── api/                  # 🌐 Endpoints FastAPI
│       │   ├── __init__.py
│       │   ├── main.py           # Aplicación FastAPI
│       │   └── routes.py         # Definición de rutas
│       │
│       ├── core/                 # 🔧 Lógica principal
│       │   ├── __init__.py
│       │   ├── language_analyzer.py
│       │   ├── security_scanner.py (futuro)
│       │   └── gemini_recommender.py (futuro)
│       │
│       ├── services/             # 💼 Capa de servicios
│       │   ├── __init__.py
│       │   ├── language_service.py
│       │   └── security_service.py (futuro)
│       │
│       ├── models/               # 📋 Esquemas de datos
│       │   ├── __init__.py
│       │   └── schemas.py        # Pydantic models
│       │
│       ├── rules/                # 📜 Reglas de vulnerabilidades
│       │   ├── __init__.py
│       │   ├── javascript_rules.py (futuro)
│       │   ├── python_rules.py (futuro)
│       │   ├── php_rules.py (futuro)
│       │   └── java_rules.py (futuro)
│       │
│       └── utils/                # 🛠️ Utilidades
│           ├── __init__.py
│           └── helpers.py
│
├── tests/                        # 🧪 Tests
│   ├── __init__.py
│   ├── test_language_analyzer.py
│   ├── test_api.py
│   └── test_gemini.py
│
├── docker/                       # 🐳 Configuración Docker
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── docs/                         # 📚 Documentación
│   ├── ARCHITECTURE.md           # Este archivo
│   ├── API.md
│   ├── SETUP.md
│   └── CONTRIBUTING.md
│
├── scripts/                      # 🚀 Scripts de utilidad
│   ├── test_gemini.py
│   └── verify.sh
│
├── config/                       # ⚙️ Configuración
│   ├── .env.example
│   └── settings.py
│
├── main.py                       # 📍 Entry point
├── requirements.txt              # 📦 Dependencias
├── setup.py                      # 📦 Setup para PyPI
├── .gitignore
├── .env.example
└── README.md
```

## Capas de la Aplicación

### 1. **Capa API (api/)**
- **Responsabilidad**: Exposición de endpoints REST
- **Archivos**:
  - `main.py`: Configuración de la aplicación FastAPI
  - `routes.py`: Definición de rutas y endpoints
  - `schemas.py`: Esquemas de validación

### 2. **Capa de Servicios (services/)**
- **Responsabilidad**: Lógica de negocio
- **Patrón**: Service Layer
- **Ejemplo**: `LanguageService` orquesta `LanguageAnalyzer`

### 3. **Capa Core (core/)**
- **Responsabilidad**: Lógica principal del dominio
- **Módulos**:
  - `LanguageAnalyzer`: Detecta lenguajes
  - `SecurityScanner`: Escanea vulnerabilidades (futuro)
  - `GeminiRecommender`: Genera recomendaciones (futuro)

### 4. **Capa de Modelos (models/)**
- **Responsabilidad**: Esquemas Pydantic para validación
- **Beneficios**: Validación automática, documentación OpenAPI

### 5. **Reglas (rules/)**
- **Responsabilidad**: Definición de patrones de vulnerabilidades
- **Estructura**: Por lenguaje de programación

## Flujo de Petición

```
Usuario/Cliente
    │
    ▼
FastAPI Endpoint (api/routes.py)
    │
    ├─ Validación (Pydantic schemas)
    │
    ▼
Service Layer (services/language_service.py)
    │
    ├─ Orquestación de lógica
    │
    ▼
Core Module (core/language_analyzer.py)
    │
    ├─ Lógica principal
    │
    ▼
Resultado/Respuesta
    │
    ▼
Cliente
```

## Ventajas de Esta Arquitectura

✅ **Escalabilidad**: Fácil agregar nuevos módulos (reglas, servicios)
✅ **Mantenibilidad**: Código organizado y separado por responsabilidades
✅ **Testabilidad**: Cada capa puede testearse independientemente
✅ **Reutilización**: Servicios podem ser usados por múltiples endpoints
✅ **Configuración**: Centralizada en `config.py`
✅ **Flexibilidad**: Fácil reemplazar implementaciones

## Patrones Utilizados

| Patrón | Ubicación | Propósito |
|--------|-----------|----------|
| **MVC** | API + Services + Core | Separación de responsabilidades |
| **Service Layer** | services/ | Lógica de negocio centralizada |
| **Factory** | Futuro en rules/ | Crear reglas por lenguaje |
| **Dependency Injection** | FastAPI | Inyectar servicios en endpoints |

## Próximas Expansiones

### FASE 2: Análisis SAST
```
core/security_scanner.py
    ├─ load_rules()
    ├─ scan_file()
    └─ analyze_patterns()

services/security_service.py
    └─ analyze_directory()

rules/
    ├─ javascript_rules.py
    ├─ python_rules.py
    ├─ php_rules.py
    └─ java_rules.py
```

### FASE 3: Integración Gemini
```
core/gemini_recommender.py
    ├─ get_security_recommendation()
    └─ analyze_code_security()

services/recommendation_service.py
    └─ generate_recommendations()

api/routes.py
    └─ POST /api/v1/recommendations
```

### FASE 4: Persistencia
```
services/storage_service.py
    ├─ store_scan()
    ├─ get_scan_history()
    └─ get_statistics()

models/database.py
    └─ MongoDB connection
```

## Consideraciones de Diseño

1. **Config Centralizada**: Evita magic strings y facilita cambios de configuración
2. **Servicios Stateless**: Permiten escalabilidad horizontal
3. **Models Tipados**: Validación automática y documentación
4. **Separación de Concerns**: Cada módulo tiene una responsabilidad clara

---

**Última actualización**: 2026-01-15

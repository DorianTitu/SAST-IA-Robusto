# ARTHEON SAST - Project Structure Guide

## Overview

This document explains the new scalable project structure implemented for ARTHEON SAST.

## Directory Organization

```
SAST-rOBUSTO/
├── src/artheon_sast/           # Main Python package
│   ├── __init__.py             # Package initialization
│   ├── config.py               # Centralized configuration
│   │
│   ├── api/                    # REST API Layer
│   │   ├── __init__.py
│   │   ├── main.py             # FastAPI application setup
│   │   └── routes.py           # API endpoints (v1)
│   │
│   ├── services/               # Business Logic Layer
│   │   ├── __init__.py
│   │   └── language_service.py # Language analysis service
│   │
│   ├── core/                   # Core Domain Logic
│   │   ├── __init__.py
│   │   └── language_analyzer.py # Language detection implementation
│   │
│   ├── models/                 # Data Models
│   │   ├── __init__.py
│   │   └── schemas.py          # Pydantic request/response models
│   │
│   ├── rules/                  # Security Rules (Future Expansion)
│   │   ├── __init__.py
│   │   ├── javascript_rules.py (future)
│   │   ├── python_rules.py (future)
│   │   ├── php_rules.py (future)
│   │   └── java_rules.py (future)
│   │
│   └── utils/                  # Utility Functions
│       ├── __init__.py
│       ├── logging.py (future)
│       ├── validators.py (future)
│       └── helpers.py (future)
│
├── tests/                      # Test Suite
│   ├── __init__.py
│   ├── test_language_analyzer.py (future)
│   ├── test_routes.py (future)
│   └── test_integration.py (future)
│
├── docker/                     # Docker Configuration
│   ├── Dockerfile             # Container image definition
│   └── docker-compose.yml     # Multi-container orchestration
│
├── docs/                       # Documentation
│   ├── ARCHITECTURE.md        # This file - Architecture overview
│   ├── API.md (future)        # API reference guide
│   ├── INSTALLATION.md (future)
│   └── CONTRIBUTING.md (future)
│
├── scripts/                    # Utility Scripts
│   ├── test_gemini.py         # Gemini API testing
│   └── verify.sh              # Verification script
│
├── config/                     # Configuration Files (Future)
│   └── logging.yaml (future)
│
├── requirements.txt           # Python dependencies
├── setup.py                   # Package installation configuration
├── pyproject.toml            # Modern Python project configuration
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
├── README.md                 # Project README
└── LICENSE                   # MIT License
```

## Architectural Layers

### 1. API Layer (`src/artheon_sast/api/`)

**Responsibility**: HTTP request handling and routing

**Components**:
- `main.py` - FastAPI app initialization, CORS setup, middleware
- `routes.py` - Endpoint definitions with request/response validation

**Key Pattern**: FastAPI routers for versioned endpoints (e.g., `/api/v1/`)

**Future Extensions**:
- Additional route files for v2, v3 endpoints
- WebSocket support for real-time scanning
- OAuth2 authentication middleware

### 2. Services Layer (`src/artheon_sast/services/`)

**Responsibility**: Business logic orchestration

**Components**:
- `language_service.py` - High-level language analysis operations
- Future services: `security_service.py`, `recommendation_service.py`, `storage_service.py`

**Key Pattern**: Services act as facades between API and Core layers

**Advantages**:
- Decouples API from implementation details
- Enables easier testing with dependency injection
- Allows code reuse across multiple endpoints

### 3. Core Layer (`src/artheon_sast/core/`)

**Responsibility**: Domain logic and algorithms

**Components**:
- `language_analyzer.py` - Language detection implementation
- Future modules: `security_scanner.py`, `gemini_recommender.py`, `report_generator.py`

**Key Pattern**: Pure domain logic, framework-agnostic

### 4. Models Layer (`src/artheon_sast/models/`)

**Responsibility**: Data validation and schema definition

**Components**:
- `schemas.py` - Pydantic models for request/response validation
- Future: Database models for MongoDB persistence

**Key Pattern**: Single source of truth for data structures

### 5. Rules Layer (`src/artheon_sast/rules/`)

**Responsibility**: Language-specific vulnerability patterns

**Current Status**: Placeholder for future implementation

**Future Structure**:
```python
# rules/javascript_rules.py
JAVASCRIPT_RULES = {
    "sql_injection": [...],
    "xss": [...],
    "command_injection": [...],
    # ... 11 security categories
}

# rules/python_rules.py
PYTHON_RULES = {
    "sql_injection": [...],
    "pickle_deserialization": [...],
    # ...
}
```

## Request Flow

```
HTTP Request
    ↓
[API Layer] routes.py
    ↓
Request Validation (Pydantic)
    ↓
[Services Layer] language_service.py
    ↓
[Core Layer] language_analyzer.py
    ↓
Domain Logic Execution
    ↓
[Models Layer] Response Construction
    ↓
[API Layer] Response Formatting
    ↓
HTTP Response
```

## Configuration Management

**File**: `src/artheon_sast/config.py`

**Includes**:
- Language file extensions mapping
- Directory ignore patterns
- API settings (title, version, description)
- Gemini model configuration
- Environment-specific settings

**Usage Pattern**:
```python
from artheon_sast.config import LANGUAGE_EXTENSIONS, IGNORE_DIRS, GEMINI_MODEL
```

## Dependency Management

**Modern Approach**:
- `pyproject.toml` - PEP 518/517/518 compliant
- `setup.py` - Compatibility layer for older tools
- `requirements.txt` - Fixed versions for Docker reproducibility

**Benefits**:
- PyPI distribution ready
- Easy version management
- Clear dependency documentation

## Testing Strategy

**Test Structure** (Future Implementation):
- Unit tests for core domain logic
- Integration tests for service layer
- End-to-end API tests
- Mock external services (Gemini, MongoDB)

## Scalability Considerations

### Phase 2-5 Expansion Points

**PHASE 2**: Add vulnerability detection
- Extend `rules/` with language-specific patterns
- Create `core/security_scanner.py`
- Add `services/security_service.py`
- New endpoint: POST `/api/v1/scan`

**PHASE 3**: Integrate Gemini recommendations
- Create `core/gemini_recommender.py`
- Create `services/recommendation_service.py`
- New endpoint: POST `/api/v1/recommendations`
- Dependency injection for API key management

**PHASE 4**: Add data persistence
- Create `models/database.py` for MongoDB schemas
- Create `services/storage_service.py`
- Implement data access layer

**PHASE 5**: Generate reports
- Create `core/report_generator.py`
- Create `services/report_service.py`
- New endpoint: GET `/api/v1/reports/{scan_id}`

### Why This Structure Scales

1. **Separation of Concerns**: Each layer has single responsibility
2. **Loose Coupling**: Changes in one layer minimize impact on others
3. **Easy Testing**: Mock dependencies at service boundaries
4. **Code Reuse**: Services can be used by multiple API endpoints
5. **Clear Contracts**: Pydantic models define precise interfaces
6. **Environment Isolation**: Core logic independent of framework

## Docker Integration

**File**: `docker/docker-compose.yml` and `docker/Dockerfile`

**Architecture**:
- Python 3.11-slim base image (minimal size)
- Dependencies installed via `requirements.txt`
- Application code copied into container
- Volume mount for host filesystem analysis
- Port 8000 exposed for API access

**Deployment Command**:
```bash
cd docker
docker-compose up --build
```

## Package Distribution

**File**: `setup.py` and `pyproject.toml`

**Future Usage**:
```bash
# Install from PyPI
pip install artheon-sast

# Use as library
from artheon_sast.services import LanguageService
service = LanguageService()
result = service.analyze_directory("/path/to/project")
```

## Development Workflow

### Adding a New Endpoint

1. **Create model** in `models/schemas.py`
2. **Add service method** in `services/` (or create new service)
3. **Add route** in `api/routes.py`
4. **Write tests** in `tests/`
5. **Update documentation** in `docs/`

### Adding a New Service Layer

1. **Create service file** in `services/new_service.py`
2. **Implement class** with clear interface
3. **Import and use** in API routes
4. **Add unit tests** in `tests/test_new_service.py`

### Adding Core Domain Logic

1. **Create module** in `core/new_module.py`
2. **Implement pure functions** (no external dependencies)
3. **Wrap in service** for API exposure
4. **Create comprehensive tests**

## Performance Considerations

- **Language Detection**: O(n) scan of directory tree
- **Caching Strategy**: Consider caching analyzed directory results
- **Async Operations**: FastAPI supports async handlers (future enhancement)
- **Database Indexing**: MongoDB indexes for fast query lookups (future)

## Security Best Practices

1. **API Key Management**: Use `.env` file (never commit `.env`)
2. **Input Validation**: All requests validated by Pydantic
3. **Directory Access**: Read-only volume mounts in Docker
4. **Rate Limiting**: Future middleware for API protection
5. **Error Handling**: Sanitized error messages to prevent info leaks

## Monitoring & Logging

**Future Implementation**:
- Structured logging in JSON format
- Application performance monitoring
- Error tracking and alerting
- Request/response metrics

## Maintenance

**Regular Tasks**:
- Update dependencies monthly
- Review security advisories
- Refactor code based on usage patterns
- Update documentation with new features

---

**Version**: 1.0  
**Last Updated**: 2024-01-20  
**Maintainer**: Dorian Tituana

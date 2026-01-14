# 🗺️ Plan de Implementación: ARTHEON-SAST Robusto + Google Gemini

## 📊 Fases de Desarrollo

### ✅ FASE 1: Backend Base con Detección de Lenguajes (COMPLETADA)
- ✔️ Backend FastAPI en Docker
- ✔️ Análisis de lenguajes (JS, Python, PHP, Java)
- ✔️ Endpoints: `/analyze` y `/analyze-files`
- ✔️ Documentación Swagger/ReDoc

**Estado:** Producción en `localhost:8000`

---

## 🔄 FASE 2: Integración SAST Completo (PRÓXIMO)

### 2.1 Crear módulo de escaneo de vulnerabilidades

**Archivos a crear:**
```
artheon_backend/
├── security_scanner.py          # Núcleo SAST
├── vulnerabilities/
│   ├── __init__.py
│   ├── js_vulnerabilities.py   # Reglas JavaScript
│   ├── py_vulnerabilities.py   # Reglas Python
│   ├── php_vulnerabilities.py  # Reglas PHP
│   └── java_vulnerabilities.py # Reglas Java
└── models.py                    # Esquemas de datos
```

### 2.2 Estructura de Regla de Vulnerabilidad

```python
{
    "rule_id": "eval_usage",
    "name": "Uso de eval()",
    "severity": "critical",
    "category": "code_injection",
    "patterns": [r"\beval\s*\(", ...],
    "description": "eval() ejecuta código arbitrario",
    "recommendations": [
        "Usar JSON.parse() en lugar de eval",
        "Validar entrada de usuario",
        "Usar bibliotecas seguras como jexl"
    ]
}
```

### 2.3 Nuevo Endpoint: Scan Completo

```bash
POST /scan
Content-Type: application/json

{
    "directory": "/app/proyecto",
    "languages": ["javascript", "python"],  # Opcional
    "severity_filter": "high"                # Opcional
}

Response:
{
    "scan_id": "scan_12345",
    "directory": "/app/proyecto",
    "status": "completed",
    "duration": 2.34,
    "vulnerabilities": [
        {
            "file": "/app/proyecto/src/app.js",
            "line": 42,
            "rule_id": "eval_usage",
            "rule_name": "Uso de eval()",
            "severity": "critical",
            "code": "eval(userInput);",
            "cwe": "CWE-95",
            "description": "...",
            "recommendations": ["..."]
        }
    ],
    "statistics": {
        "total_files": 45,
        "total_vulnerabilities": 27,
        "by_severity": {
            "critical": 5,
            "high": 12,
            "medium": 8,
            "low": 2
        }
    }
}
```

---

## 🤖 FASE 3: Integración Google Gemini API

### 3.1 Configuración

```python
# .env
GOOGLE_API_KEY=your-api-key-here

# requirements.txt
google-generativeai==0.3.0
python-dotenv==1.0.0
```

### 3.2 Nuevo Módulo: `gemini_recommender.py`

```python
import google.generativeai as genai

class GeminiRecommender:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def get_fix_recommendations(
        self, 
        vulnerability: dict,
        code_context: str
    ) -> dict:
        """
        Obtiene recomendaciones de corrección usando Google Gemini
        
        Args:
            vulnerability: Información de vulnerabilidad detectada
            code_context: Código completo del archivo
        
        Returns:
            Recomendaciones generadas por Gemini
        """
        prompt = f"""
        Analiza esta vulnerabilidad de seguridad y proporciona soluciones:
        
        Vulnerabilidad: {vulnerability['rule_name']}
        Lenguaje: {vulnerability['language']}
        Línea: {vulnerability['code']}
        Descripción: {vulnerability['description']}
        
        Código contexto:
        {code_context}
        
        Por favor proporciona:
        1. Explicación del problema
        2. 3 formas diferentes de arreglarlo
        3. Código de ejemplo corregido
        4. Referencias de seguridad
        """
        
        response = self.model.generate_content(prompt)
        return {
            "recommendations": response.text,
            "model": "gemini-pro",
            "tokens_used": response.usage_metadata
        }
```

### 3.3 Nuevo Endpoint: Recomendaciones

```bash
POST /recommendations
Content-Type: application/json

{
    "vulnerability": {
        "rule_id": "eval_usage",
        "rule_name": "Uso de eval()",
        "language": "javascript",
        "code": "eval(userInput);",
        "severity": "critical"
    },
    "code_context": "const x = eval(userInput); ..."
}

Response:
{
    "recommendation_id": "rec_12345",
    "vulnerability": "eval_usage",
    "solutions": [
        {
            "title": "Usar JSON.parse()",
            "description": "...",
            "code_example": "const x = JSON.parse(input);",
            "score": 0.95
        },
        {
            "title": "Usar Function Constructor",
            "description": "...",
            "code_example": "new Function(input)(...)",
            "score": 0.75
        }
    ],
    "generated_by": "Google Gemini Pro"
}
```

---

## 💾 FASE 4: Persistencia con MongoDB (Opcional)

### 4.1 Conexión MongoDB

```python
from pymongo import MongoClient

class MongoStorage:
    def __init__(self, uri: str):
        self.client = MongoClient(uri)
        self.db = self.client['artheon_sast']
    
    def store_scan(self, scan_result: dict):
        """Almacena resultado de escaneo"""
        self.db.scans.insert_one(scan_result)
    
    def get_scan_history(self, directory: str):
        """Obtiene histórico de escaneos"""
        return list(self.db.scans.find({"directory": directory}))
```

### 4.2 Endpoints de Histórico

```bash
GET /scans
GET /scans/{scan_id}
DELETE /scans/{scan_id}
```

---

## 📊 FASE 5: Reportes HTML Interactivos

### 5.1 Endpoint: Generar Reporte

```bash
GET /report/{scan_id}?format=html

Response: HTML con:
- Gráficos de severidad
- Tabla de vulnerabilidades interactiva
- Recomendaciones del modelo
- Exporta a JSON/PDF
```

### 5.2 Características

```html
<div id="summary">
    <!-- Metrics: Critical, High, Medium, Low -->
    <div class="severity-badge critical">5 CRITICAL</div>
    <div class="severity-badge high">12 HIGH</div>
</div>

<div id="vulnerabilities">
    <!-- Tabla expandible con código y recomendaciones -->
    <table>
        <tr>
            <td>src/app.js:42</td>
            <td>eval_usage</td>
            <td>CRITICAL</td>
            <td><button>Ver Recomendaciones</button></td>
        </tr>
    </table>
</div>
```

---

## 🎯 Implementación Step-by-Step

### Paso 1: Crear módulos SAST

```bash
# En artheon_backend/
python -m pip install -r requirements.txt  # Ya tiene FastAPI

# Crear security_scanner.py
# Crear vulnerabilities/js_vulnerabilities.py
# Crear vulnerabilities/py_vulnerabilities.py
# etc.
```

### Paso 2: Agregar endpoint /scan

```python
@app.post("/scan", response_model=ScanResponse)
async def scan_directory(request: ScanRequest):
    analyzer = LanguageAnalyzer(request.directory)
    analysis = analyzer.analyze()
    
    scanner = SecurityScanner(request.directory)
    vulnerabilities = scanner.scan()
    
    return {
        "scan_id": str(uuid.uuid4()),
        "vulnerabilities": vulnerabilities,
        "statistics": calculate_stats(vulnerabilities)
    }
```

### Paso 3: Integrar Google Gemini

```bash
pip install google-generativeai

# Crear gemini_recommender.py
# Agregar endpoint /recommendations
```

### Paso 4: Agregar almacenamiento

```bash
pip install pymongo

# Crear mongo_storage.py
# Agregar endpoints de histórico
```

### Paso 5: Generar reportes

```bash
# Crear html_reporter.py
# Agregar endpoint /report
```

---

## 📦 Dependencias Finales

```txt
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
python-multipart==0.0.6
google-generativeai==0.3.0
pymongo==4.6.0
python-dotenv==1.0.0
jinja2==3.1.2
```

---

## 🧪 Testing

```bash
# Unit tests
pytest tests/test_security_scanner.py
pytest tests/test_gemini_recommender.py

# Integration tests
pytest tests/test_api.py
```

---

## 🚀 Deployment

### Docker Compose Final

```yaml
version: '3.8'

services:
  artheon-backend:
    build: .
    ports:
      - "8000:8000"
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - MONGODB_URI=${MONGODB_URI}
    volumes:
      - /:/host:ro
  
  mongodb:
    image: mongo:7.0
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db

volumes:
  mongodb_data:
```

---

## 📈 Roadmap Visual

```
┌─────────────────────────────────────────────────────────┐
│ FASE 1: Backend Base ✅ (ACTUAL)                        │
├─────────────────────────────────────────────────────────┤
│ FASE 2: SAST Completo 🔄 (PRÓXIMO)                     │
├─────────────────────────────────────────────────────────┤
│ FASE 3: Google Gemini 🤖 (PRÓXIMO)                     │
├─────────────────────────────────────────────────────────┤
│ FASE 4: MongoDB 💾 (OPCIONAL)                          │
├─────────────────────────────────────────────────────────┤
│ FASE 5: Reportes 📊 (FINAL)                            │
└─────────────────────────────────────────────────────────┘
```

---

## 💡 Notas Importantes

1. **Google Gemini API Key**: Obtén en `https://ai.google.dev`
2. **MongoDB**: Usa MongoDB Atlas (cloud) o local
3. **Rate Limiting**: Implementa rate limiting para Gemini
4. **Caché**: Cachea respuestas de Gemini para vulnerabilidades similares
5. **Error Handling**: Manejar fallos de Gemini API con fallback

---

## 👤 Autor
ARTHEON-SAST Project - 2026

**Estado**: Backend base completo ✅ | Listo para SAST + Gemini 🚀

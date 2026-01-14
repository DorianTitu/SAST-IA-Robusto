# 🚀 ARTHEON-SAST: Guía de Inicio Rápido

## 📍 TU ESTADO ACTUAL

✅ **Backend FastAPI está corriendo en puerto 8000**

```
🐳 Contenedor: artheon-sast-backend
🌐 URL: http://localhost:8000
📚 Documentación: http://localhost:8000/docs
🔧 Estado: OPERACIONAL
```

---

## ⚡ Lo Puedes Hacer AHORA

### 1. Acceder a la Documentación Interactiva
```bash
open http://localhost:8000/docs
# O en Firefox/Chrome:
# http://localhost:8000/docs
```

### 2. Probar Endpoints
```bash
# Health Check
curl http://localhost:8000/health

# Analizar Lenguajes
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"directory": "/app/test_project"}'

# Listar Archivos
curl -X POST http://localhost:8000/analyze-files \
  -H "Content-Type: application/json" \
  -d '{"directory": "/app/test_project"}'
```

### 3. Ver Logs del Contenedor
```bash
docker logs artheon-sast-backend -f
```

---

## 📂 Archivos Importantes

| Archivo | Propósito |
|---------|----------|
| `README.md` | Documentación principal del proyecto |
| `IMPLEMENTATION_PLAN.md` | Plan de 5 fases de desarrollo |
| `PROJECT_SUMMARY.md` | Resumen detallado de lo completado |
| `verify.sh` | Script de verificación (20/20 ✓) |
| `artheon_backend/main.py` | Código del API FastAPI |
| `artheon_backend/language_analyzer.py` | Módulo de análisis |

---

## 🎯 Próximos Pasos (FASE 2)

Para **agregar escaneo de vulnerabilidades**, necesitas:

### Paso 1: Crear módulos de vulnerabilidades

```bash
cd artheon_backend

# Crear archivo de escaneo
cat > security_scanner.py << 'EOF'
import re
from pathlib import Path

class SecurityScanner:
    def __init__(self, directory):
        self.directory = Path(directory)
    
    def scan(self):
        vulnerabilities = []
        # Implementar lógica de escaneo
        return vulnerabilities
EOF
```

### Paso 2: Crear archivo de reglas (ejemplo)

```bash
cat > vulnerabilities_js.py << 'EOF'
JAVASCRIPT_RULES = {
    "eval_usage": {
        "name": "Uso de eval()",
        "severity": "critical",
        "patterns": [r"\beval\s*\("],
        "description": "eval() ejecuta código arbitrario"
    }
}
EOF
```

### Paso 3: Agregar endpoint a main.py

```python
@app.post("/scan")
async def scan_directory(request: AnalyzeRequest):
    scanner = SecurityScanner(request.directory)
    results = scanner.scan()
    return {
        "vulnerabilities": results,
        "total": len(results)
    }
```

---

## 🤖 Integración Google Gemini (FASE 3)

```bash
# 1. Obtener API Key en: https://ai.google.dev

# 2. Instalar librería
pip install google-generativeai

# 3. Crear gemini_recommender.py
cat > artheon_backend/gemini_recommender.py << 'EOF'
import google.generativeai as genai

class GeminiRecommender:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
    
    def get_recommendations(self, vulnerability):
        prompt = f"Cómo arreglar: {vulnerability['name']}"
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
EOF

# 4. Agregar endpoint /recommendations a main.py
```

---

## 📊 Verificar Todo Está OK

```bash
# Ejecutar verificación completa
cd /Users/doriantituana/Desktop/Dorian/Tesis/SAST-rOBUSTO
bash verify.sh

# Resultado esperado:
# ✓ 20/20 checks pasados
```

---

## 🐳 Comandos Docker Útiles

```bash
# Ver si está corriendo
docker ps | grep artheon

# Reiniciar
docker-compose -f artheon_backend/docker-compose.yml restart

# Reconstruir
docker-compose -f artheon_backend/docker-compose.yml up --build -d

# Ver logs
docker logs artheon-sast-backend

# Conectar a bash
docker exec -it artheon-sast-backend bash

# Detener
docker-compose -f artheon_backend/docker-compose.yml down
```

---

## 📚 Documentación de Referencia

- 📖 [README.md](README.md) - Documentación general
- 📋 [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) - Plan completo
- 📝 [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Resumen ejecutivo
- 🚀 [artheon_backend/QUICKSTART.md](artheon_backend/QUICKSTART.md) - Guía del backend
- 🔧 [artheon_backend/README.md](artheon_backend/README.md) - Detalles técnicos

---

## 💻 Ejemplos Python

```python
import requests
import json

API = "http://localhost:8000"

# Analizar directorio
response = requests.post(
    f"{API}/analyze",
    json={"directory": "/app/proyecto"}
)

if response.status_code == 200:
    data = response.json()
    
    print("🔍 Análisis Completado")
    print(f"Lenguajes: {', '.join(data['languages_detected'])}")
    print(f"Archivos totales: {data['total_files']}")
    
    print("\n📊 Detalles:")
    for lang, details in data['language_details'].items():
        print(f"  {lang}: {details['files']} archivos - {details['extensions']}")
```

---

## 🔗 URLs Útiles

| Recurso | URL |
|---------|-----|
| **API Swagger** | http://localhost:8000/docs |
| **API ReDoc** | http://localhost:8000/redoc |
| **API Root** | http://localhost:8000 |
| **Health Check** | http://localhost:8000/health |
| **Google Gemini** | https://ai.google.dev |
| **FastAPI Docs** | https://fastapi.tiangolo.com/ |

---

## ❓ Solución de Problemas

### El API no responde
```bash
# Verificar que Docker esté corriendo
docker ps | grep artheon

# Si no aparece, reiniciar
cd artheon_backend
docker-compose up -d
```

### Puerto 8000 en uso
```bash
# Ver qué está usando el puerto
lsof -i :8000

# Cambiar puerto en docker-compose.yml:
# ports: ["8001:8000"]
```

### Error "No such file or directory"
```bash
# Asegúrate que el directorio existe
ls -la /ruta/que/intentes/analizar

# Dentro del contenedor, usa /app/... o /host/Users/...
```

---

## 📈 Checklist de Próximos Pasos

- [ ] Revisar [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md)
- [ ] Implementar FASE 2: Escaneo SAST
- [ ] Crear reglas de vulnerabilidades
- [ ] Agregar endpoint `/scan`
- [ ] Instalar Google Generative AI SDK
- [ ] Obtener API Key de Google
- [ ] Implementar FASE 3: Gemini API
- [ ] Agregar endpoint `/recommendations`
- [ ] Configurar MongoDB (opcional)
- [ ] Crear generador de reportes HTML
- [ ] Agregar tests unitarios
- [ ] Documentar API final

---

## 🎓 Recursos Recomendados

- **FastAPI Tutorial**: https://fastapi.tiangolo.com/tutorial/
- **Docker Guide**: https://docs.docker.com/get-started/
- **Python Regex**: https://docs.python.org/3/library/re.html
- **Google Gemini API**: https://ai.google.dev/docs/

---

## 📞 Ayuda Rápida

**¿Backend no inicia?**
```bash
docker logs artheon-sast-backend
```

**¿Puerto en conflicto?**
```bash
lsof -i :8000
kill -9 <PID>
```

**¿Reconstruir imagen?**
```bash
docker-compose -f artheon_backend/docker-compose.yml down
docker-compose -f artheon_backend/docker-compose.yml up --build -d
```

**¿Verificar todo OK?**
```bash
bash verify.sh
```

---

## 🎉 ¡LISTO!

Tu backend ARTHEON-SAST está:
- ✅ Corriendo en Docker
- ✅ Respondiendo en puerto 8000
- ✅ Con 3 endpoints funcionales
- ✅ Documentado completamente
- 🚀 Listo para FASE 2

**¡Comienza con la FASE 2 cuando estés listo!**

---

**Última Actualización**: 2026-01-14  
**Estado**: ✅ OPERACIONAL

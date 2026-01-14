"""
ARTHEON-SAST Backend API
Backend FastAPI para análisis estático de seguridad
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(__file__))

from language_analyzer import LanguageAnalyzer

# Crear aplicación FastAPI
app = FastAPI(
    title="ARTHEON-SAST Backend",
    description="Backend para análisis estático de vulnerabilidades",
    version="1.0.0"
)

# Modelos Pydantic
class AnalyzeRequest(BaseModel):
    """Modelo para solicitud de análisis"""
    directory: str
    
    class Config:
        example = {
            "directory": "/path/to/project"
        }


class LanguageInfo(BaseModel):
    """Información de un lenguaje detectado"""
    files: int
    extensions: list


class AnalyzeResponse(BaseModel):
    """Modelo para respuesta de análisis"""
    directory: str
    languages_detected: list
    language_details: dict
    total_files: int
    supported: bool


# Rutas

@app.get("/", tags=["Health"])
async def root():
    """Endpoint raíz - verificar que el API está activo"""
    return {
        "message": "🛡️ ARTHEON-SAST Backend API",
        "status": "active",
        "version": "1.0.0",
        "documentation": "/docs"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Verificar estado de la aplicación"""
    return {
        "status": "healthy",
        "service": "ARTHEON-SAST Backend"
    }


@app.post("/analyze", response_model=AnalyzeResponse, tags=["Analysis"])
async def analyze_directory(request: AnalyzeRequest):
    """
    Analiza un directorio para detectar lenguajes de programación
    
    **Parámetros:**
    - `directory`: Ruta absoluta del directorio a analizar
    
    **Retorna:**
    - `directory`: Directorio analizado
    - `languages_detected`: Lista de lenguajes encontrados
    - `language_details`: Detalles por lenguaje (cantidad de archivos y extensiones)
    - `total_files`: Total de archivos encontrados
    - `supported`: Si contiene lenguajes soportados
    
    **Ejemplo de uso:**
    ```json
    {
        "directory": "/Users/user/mi-proyecto"
    }
    ```
    
    **Respuesta exitosa (200):**
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
    """
    try:
        # Validar que el directorio no esté vacío
        if not request.directory or not request.directory.strip():
            raise HTTPException(
                status_code=400,
                detail="El campo 'directory' no puede estar vacío"
            )
        
        # Crear analizador
        analyzer = LanguageAnalyzer(request.directory)
        
        # Realizar análisis
        result = analyzer.analyze()
        
        return AnalyzeResponse(**result)
    
    except ValueError as e:
        # Error de validación del directorio
        raise HTTPException(
            status_code=404,
            detail=f"Error: {str(e)}"
        )
    
    except Exception as e:
        # Error inesperado
        raise HTTPException(
            status_code=500,
            detail=f"Error interno del servidor: {str(e)}"
        )


@app.post("/analyze-files", tags=["Analysis"])
async def analyze_files(request: AnalyzeRequest):
    """
    Retorna lista detallada de todos los archivos por lenguaje
    
    **Parámetros:**
    - `directory`: Ruta absoluta del directorio a analizar
    
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
    """
    try:
        if not request.directory or not request.directory.strip():
            raise HTTPException(
                status_code=400,
                detail="El campo 'directory' no puede estar vacío"
            )
        
        analyzer = LanguageAnalyzer(request.directory)
        analysis = analyzer.analyze()
        
        files_by_language = {}
        for language in analysis['languages_detected']:
            files_by_language[language] = analyzer.get_files_by_language(language)
        
        return {
            "directory": request.directory,
            "files_by_language": files_by_language
        }
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


# Configuración para ejecución directa
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )

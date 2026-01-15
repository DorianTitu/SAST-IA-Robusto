"""
Rutas de la API
"""

from fastapi import APIRouter, HTTPException

from ..models.schemas import AnalyzeRequest, AnalyzeResponse
from ..services.language_service import LanguageService

router = APIRouter(prefix="/api/v1", tags=["Analysis"])

language_service = LanguageService()


@router.post("/analyze", response_model=AnalyzeResponse, tags=["Analysis"])
async def analyze_directory(request: AnalyzeRequest):
    """
    Analiza un directorio para detectar lenguajes de programación
    
    **Parámetros:**
    - `directory`: Ruta absoluta del directorio a analizar
    
    **Retorna:**
    - `directory`: Directorio analizado
    - `languages_detected`: Lista de lenguajes encontrados
    - `language_details`: Detalles por lenguaje
    - `total_files`: Total de archivos encontrados
    - `supported`: Si contiene lenguajes soportados
    """
    try:
        if not request.directory or not request.directory.strip():
            raise HTTPException(
                status_code=400,
                detail="El campo 'directory' no puede estar vacío"
            )
        
        result = language_service.analyze_directory(request.directory)
        return AnalyzeResponse(**result)
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


@router.post("/analyze-files", tags=["Analysis"])
async def analyze_files(request: AnalyzeRequest):
    """
    Retorna lista detallada de todos los archivos por lenguaje
    """
    try:
        if not request.directory or not request.directory.strip():
            raise HTTPException(status_code=400, detail="El campo 'directory' no puede estar vacío")
        
        result = language_service.get_files_by_language(request.directory)
        return {
            "directory": request.directory,
            "files_by_language": result
        }
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

"""
Esquemas Pydantic para validación de datos
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class AnalyzeRequest(BaseModel):
    """Solicitud de análisis de directorio"""
    directory: str = Field(..., description="Ruta absoluta del directorio a analizar")
    
    class Config:
        json_schema_extra = {
            "example": {
                "directory": "/path/to/project"
            }
        }


class LanguageInfo(BaseModel):
    """Información de un lenguaje detectado"""
    files: int = Field(..., description="Cantidad de archivos")
    extensions: List[str] = Field(..., description="Extensiones encontradas")


class AnalyzeResponse(BaseModel):
    """Respuesta del análisis de directorio"""
    directory: str
    languages_detected: List[str]
    language_details: Dict[str, LanguageInfo]
    total_files: int
    supported: bool


class AnalyzeFilesResponse(BaseModel):
    """Respuesta con lista de archivos por lenguaje"""
    directory: str
    files_by_language: Dict[str, List[str]]


class VulnerabilityRequest(BaseModel):
    """Solicitud de recomendación para una vulnerabilidad"""
    name: str
    language: str
    severity: str
    description: str
    code: str
    cwe: Optional[str] = None


class VulnerabilityRecommendation(BaseModel):
    """Recomendación de seguridad para una vulnerabilidad"""
    vulnerability: str
    recommendation: str
    solutions: Optional[List[Dict]] = None
    code_example: Optional[str] = None

"""
Módulo principal de la aplicación FastAPI
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from ..config import API_TITLE, API_DESCRIPTION, API_VERSION
from ..models.schemas import AnalyzeRequest, AnalyzeResponse
from ..core.language_analyzer import LanguageAnalyzer
from .routes import router

# Crear aplicación FastAPI
app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Agregar CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(router)


# Rutas raíz
@app.get("/", tags=["Health"])
async def root():
    """Endpoint raíz - verificar que el API está activo"""
    return {
        "message": "🛡️ ARTHEON-SAST Backend API",
        "status": "active",
        "version": API_VERSION,
        "documentation": "/docs"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Verificar estado de la aplicación"""
    return {
        "status": "healthy",
        "service": "ARTHEON-SAST Backend"
    }

"""
Módulo de configuración de la aplicación
"""

import os
from typing import List, Set

# Configuración de lenguajes soportados
SUPPORTED_LANGUAGES = {'javascript', 'python', 'php', 'java'}

# Mapeo de extensiones a lenguajes
LANGUAGE_EXTENSIONS = {
    'javascript': {'.js', '.jsx', '.ts', '.tsx', '.mjs', '.cjs'},
    'python': {'.py', '.pyw', '.pyi'},
    'php': {'.php', '.php3', '.php4', '.php5', '.php7', '.php8', '.phtml', '.phps'},
    'java': {'.java'},
}

# Directorios a ignorar
IGNORE_DIRS = {
    '.git', '.gitignore', 'node_modules', 'venv', '__pycache__',
    '.idea', '.vscode', 'dist', 'build', 'target', '.gradle',
    '.pytest_cache', '.tox', 'vendor', 'coverage', '.egg-info',
    '.venv', 'env', 'ENV', 'venv3', '.mypy_cache', '.django_cache'
}

# Configuración de Google Gemini
GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Configuración de API
API_TITLE = "🛡️ ARTHEON-SAST Backend"
API_DESCRIPTION = "Static Application Security Testing con Google Gemini"
API_VERSION = "1.0.0"

# Configuración de servidor
HOST = "0.0.0.0"
PORT = 8000
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Configuración MongoDB (futuro)
MONGODB_URI = os.getenv("MONGODB_URI", "")
MONGODB_DB_NAME = "artheon_sast"

# Configuración de reportes
REPORT_OUTPUT_DIR = os.getenv("REPORT_OUTPUT_DIR", "./reports")

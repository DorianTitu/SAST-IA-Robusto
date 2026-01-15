"""
🛡️ ARTHEON-SAST - Static Application Security Testing
Herramienta de análisis estático de vulnerabilidades con AI
"""

__version__ = "1.0.0"
__author__ = "Dorian Tituana"
__description__ = "Static Application Security Testing con Google Gemini"

from .core.language_analyzer import LanguageAnalyzer

__all__ = ["LanguageAnalyzer"]

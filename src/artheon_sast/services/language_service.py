"""
Servicio de lenguajes
Capa de lógica de negocio para análisis de lenguajes
"""

from typing import Dict, List

from ..core.language_analyzer import LanguageAnalyzer


class LanguageService:
    """Servicio para operaciones relacionadas con lenguajes"""
    
    def analyze_directory(self, directory: str) -> Dict:
        """
        Analiza un directorio
        
        Args:
            directory: Ruta del directorio
        
        Returns:
            Resultado del análisis
        """
        analyzer = LanguageAnalyzer(directory)
        return analyzer.analyze()
    
    def get_files_by_language(self, directory: str) -> Dict[str, List[str]]:
        """
        Obtiene archivos agrupados por lenguaje
        
        Args:
            directory: Ruta del directorio
        
        Returns:
            Diccionario con archivos por lenguaje
        """
        analyzer = LanguageAnalyzer(directory)
        analysis = analyzer.analyze()
        
        files_by_language = {}
        for language in analysis['languages_detected']:
            files_by_language[language] = analyzer.get_files_by_language(language)
        
        return files_by_language

"""
Language Analyzer Module
Detecta qué lenguajes de programación están presentes en un directorio
"""

import os
from pathlib import Path
from typing import Dict, List, Set

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
    '.pytest_cache', '.tox', 'vendor', 'coverage', '.egg-info'
}


class LanguageAnalyzer:
    """Analiza un directorio para detectar lenguajes presentes"""

    def __init__(self, directory: str):
        """
        Inicializa el analizador
        
        Args:
            directory: Ruta del directorio a analizar
        
        Raises:
            ValueError: Si el directorio no existe
        """
        self.directory = Path(directory)
        
        if not self.directory.exists():
            raise ValueError(f"Directorio no existe: {directory}")
        
        if not self.directory.is_dir():
            raise ValueError(f"La ruta no es un directorio: {directory}")

    def analyze(self) -> Dict:
        """
        Analiza el directorio y detecta lenguajes presentes
        
        Returns:
            Dict con estructura:
            {
                'directory': '/ruta/analizada',
                'languages_detected': ['javascript', 'python'],
                'language_details': {
                    'javascript': {
                        'files': 5,
                        'extensions': ['.js', '.ts']
                    },
                    'python': {
                        'files': 3,
                        'extensions': ['.py']
                    }
                },
                'total_files': 8,
                'supported': True
            }
        """
        detected_languages: Set[str] = set()
        language_details: Dict = {}
        
        # Recorrer directorio recursivamente
        for root, dirs, files in os.walk(self.directory):
            # Filtrar directorios ignorados
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            
            for file in files:
                file_ext = Path(file).suffix.lower()
                
                # Buscar en qué lenguaje pertenece esta extensión
                for language, extensions in LANGUAGE_EXTENSIONS.items():
                    if file_ext in extensions:
                        detected_languages.add(language)
                        
                        # Inicializar detalles si es primera vez
                        if language not in language_details:
                            language_details[language] = {
                                'files': 0,
                                'extensions': set()
                            }
                        
                        # Incrementar contador y agregar extensión
                        language_details[language]['files'] += 1
                        language_details[language]['extensions'].add(file_ext)
                        break
        
        # Convertir sets a listas para serialización JSON
        for lang in language_details:
            language_details[lang]['extensions'] = sorted(
                list(language_details[lang]['extensions'])
            )
        
        total_files = sum(detail['files'] for detail in language_details.values())
        
        return {
            'directory': str(self.directory),
            'languages_detected': sorted(list(detected_languages)),
            'language_details': language_details,
            'total_files': total_files,
            'supported': len(detected_languages) > 0
        }

    def get_file_count(self, language: str) -> int:
        """Obtiene cantidad de archivos de un lenguaje específico"""
        analysis = self.analyze()
        return analysis['language_details'].get(language, {}).get('files', 0)

    def get_files_by_language(self, language: str) -> List[str]:
        """
        Obtiene lista de archivos de un lenguaje específico
        
        Args:
            language: Lenguaje a buscar (ej: 'javascript', 'python')
        
        Returns:
            Lista de rutas de archivos
        """
        if language not in LANGUAGE_EXTENSIONS:
            return []
        
        extensions = LANGUAGE_EXTENSIONS[language]
        files = []
        
        for root, dirs, filenames in os.walk(self.directory):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            
            for file in filenames:
                if Path(file).suffix.lower() in extensions:
                    files.append(os.path.join(root, file))
        
        return sorted(files)

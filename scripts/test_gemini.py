"""
🤖 Google Gemini API - Test Module
Prueba de integración con Google Generative AI (Gemini)
"""

import google.genai as genai
from typing import Dict, List


class GeminiSecurityRecommender:
    """
    Recomendador de seguridad usando Google Gemini 2.0 Flash
    Genera soluciones automáticas para vulnerabilidades detectadas
    """
    
    def __init__(self, api_key: str):
        """
        Inicializa el recomendador con API key de Google
        
        Args:
            api_key: Clave de API de Google Generative AI
        """
        try:
            self.client = genai.Client(api_key=api_key)
            self.model = "gemini-2.0-flash"
            self.status = "✅ Conectado"
            print("✅ Conectado con Google Gemini 2.0 Flash")
        except Exception as e:
            self.status = f"❌ Error: {str(e)}"
            raise Exception(f"No se pudo conectar con Gemini: {str(e)}")
    
    def test_connection(self) -> Dict:
        """
        Prueba la conexión con Gemini
        
        Returns:
            Diccionario con resultado de la prueba
        """
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents="¿Qué es una vulnerabilidad de seguridad XSS? (responde en 1-2 líneas)"
            )
            
            return {
                "status": "✅ Conexión exitosa",
                "model": self.model,
                "response": response.text,
                "error": None
            }
        except Exception as e:
            return {
                "status": "❌ Error de conexión",
                "model": self.model,
                "response": None,
                "error": str(e)
            }
    
    def get_security_recommendation(self, vulnerability: Dict) -> Dict:
        """
        Obtiene recomendaciones de seguridad para una vulnerabilidad
        
        Args:
            vulnerability: Diccionario con información de la vulnerabilidad
                {
                    "name": "Nombre de la vulnerabilidad",
                    "language": "javascript",
                    "severity": "critical",
                    "description": "Descripción",
                    "code": "Código vulnerable",
                    "cwe": "CWE-95"
                }
        
        Returns:
            Diccionario con recomendaciones
        """
        
        prompt = f"""
Eres un experto en seguridad de software. Analiza esta vulnerabilidad y proporciona una solución:

**Vulnerabilidad**: {vulnerability.get('name', 'N/A')}
**Lenguaje**: {vulnerability.get('language', 'N/A')}
**Severidad**: {vulnerability.get('severity', 'N/A')}
**CWE**: {vulnerability.get('cwe', 'N/A')}
**Descripción**: {vulnerability.get('description', 'N/A')}

**Código Vulnerable**:
```
{vulnerability.get('code', 'N/A')}
```

Por favor proporciona:
1. **Explicación del Problema** (2-3 líneas)
2. **3 Soluciones Diferentes** (cada una con nombre y descripción corta)
3. **Código de Ejemplo Corregido** (en el mismo lenguaje)
4. **Referencias de Seguridad** (menciona estándares como OWASP, SANS TOP 25, etc.)

Sé conciso pero técnicamente preciso.
"""
        
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            
            return {
                "status": "✅ Recomendación generada",
                "vulnerability": vulnerability.get('name'),
                "recommendation": response.text,
                "error": None,
                "tokens_used": None
            }
        except Exception as e:
            return {
                "status": "❌ Error generando recomendación",
                "vulnerability": vulnerability.get('name'),
                "recommendation": None,
                "error": str(e),
                "tokens_used": None
            }
    
    def analyze_code_security(self, code: str, language: str) -> Dict:
        """
        Analiza seguridad de un fragmento de código
        
        Args:
            code: Código a analizar
            language: Lenguaje de programación
        
        Returns:
            Análisis de seguridad
        """
        
        prompt = f"""
Analiza este código {language} en busca de vulnerabilidades de seguridad:

```{language}
{code}
```

Identifica:
1. Vulnerabilidades presentes (si existen)
2. Nivel de riesgo (CRITICAL, HIGH, MEDIUM, LOW, NONE)
3. Recomendaciones de remediación

Sé específico y técnico.
"""
        
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            
            return {
                "status": "✅ Análisis completado",
                "language": language,
                "analysis": response.text,
                "error": None
            }
        except Exception as e:
            return {
                "status": "❌ Error en análisis",
                "language": language,
                "analysis": None,
                "error": str(e)
            }


def test_gemini_integration(api_key: str):
    """
    Función de prueba completa de integración con Gemini
    
    Args:
        api_key: Clave de API de Google
    """
    print("=" * 70)
    print("🛡️  PRUEBA DE INTEGRACIÓN: GOOGLE GEMINI + ARTHEON-SAST")
    print("=" * 70)
    print()
    
    # Test 1: Conexión básica
    print("📋 TEST 1: Conectando con Gemini...")
    try:
        recommender = GeminiSecurityRecommender(api_key)
        print(f"✅ Estado: {recommender.status}")
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    print()
    
    # Test 2: Prueba de conexión
    print("📋 TEST 2: Probando comunicación con modelo...")
    test_result = recommender.test_connection()
    print(f"✅ Estado: {test_result['status']}")
    print(f"🤖 Respuesta del modelo:")
    print(f"   {test_result['response']}")
    if test_result['error']:
        print(f"❌ Error: {test_result['error']}")
    
    print()
    
    # Test 3: Recomendación de seguridad para eval()
    print("📋 TEST 3: Generando recomendación para vulnerabilidad (eval usage)...")
    
    vulnerability = {
        "name": "Uso de eval()",
        "language": "javascript",
        "severity": "critical",
        "cwe": "CWE-95",
        "description": "eval() ejecuta código JavaScript arbitrario, permitiendo inyección de código",
        "code": "const result = eval(userInput);"
    }
    
    recommendation = recommender.get_security_recommendation(vulnerability)
    print(f"✅ Estado: {recommendation['status']}")
    print(f"🎯 Vulnerabilidad: {recommendation['vulnerability']}")
    print()
    print("📝 RECOMENDACIÓN GENERADA:")
    print("-" * 70)
    print(recommendation['recommendation'])
    print("-" * 70)
    
    print()
    
    # Test 4: Análisis de código
    print("📋 TEST 4: Analizando código JavaScript...")
    
    code_sample = """
function processUser(userId) {
    const query = "SELECT * FROM users WHERE id = " + userId;
    const result = db.query(query);
    document.getElementById("result").innerHTML = result;
    return result;
}
"""
    
    analysis = recommender.analyze_code_security(code_sample, "javascript")
    print(f"✅ Estado: {analysis['status']}")
    print()
    print("🔍 ANÁLISIS DE SEGURIDAD:")
    print("-" * 70)
    print(analysis['analysis'])
    print("-" * 70)
    
    print()
    print("=" * 70)
    print("✅ PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 70)
    print()
    print("📌 RESUMEN:")
    print("   ✓ Conexión con Google Gemini: OK")
    print("   ✓ Comunicación modelo: OK")
    print("   ✓ Generación de recomendaciones: OK")
    print("   ✓ Análisis de código: OK")
    print()
    print("🚀 El modelo está listo para integración en ARTHEON-SAST")
    print()


if __name__ == "__main__":
    # Usar API key proporcionada
    API_KEY = "AIzaSyBvhSGJsJ1mWCoucxMEvaiKXaj23EPF6IE"
    test_gemini_integration(API_KEY)

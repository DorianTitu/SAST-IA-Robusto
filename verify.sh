#!/bin/bash

# 🛡️ ARTHEON-SAST Backend - Script de Verificación

echo "=================================================="
echo "🛡️  ARTHEON-SAST Backend - Verification Script"
echo "=================================================="
echo ""

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Contador de checks
PASSED=0
TOTAL=0

# Función para verificar
check() {
    TOTAL=$((TOTAL + 1))
    local desc="$1"
    local condition="$2"
    
    if eval "$condition"; then
        echo -e "${GREEN}✓${NC} $desc"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}✗${NC} $desc"
    fi
}

# Verificaciones de archivos
echo -e "${BLUE}📁 Verificando estructura de archivos...${NC}"
check "README.md existe" "[ -f README.md ]"
check "IMPLEMENTATION_PLAN.md existe" "[ -f IMPLEMENTATION_PLAN.md ]"
check "artheon_backend/ existe" "[ -d artheon_backend ]"
check "artheon_backend/main.py existe" "[ -f artheon_backend/main.py ]"
check "artheon_backend/language_analyzer.py existe" "[ -f artheon_backend/language_analyzer.py ]"
check "artheon_backend/Dockerfile existe" "[ -f artheon_backend/Dockerfile ]"
check "artheon_backend/docker-compose.yml existe" "[ -f artheon_backend/docker-compose.yml ]"
check "artheon_backend/requirements.txt existe" "[ -f artheon_backend/requirements.txt ]"
check "artheon_backend/README.md existe" "[ -f artheon_backend/README.md ]"
check "artheon_backend/QUICKSTART.md existe" "[ -f artheon_backend/QUICKSTART.md ]"

echo ""
echo -e "${BLUE}🐳 Verificando Docker...${NC}"
check "Docker daemon está corriendo" "docker ps >/dev/null 2>&1"
check "Docker image está construida" "docker images | grep artheon_backend >/dev/null 2>&1"
check "Contenedor está corriendo" "docker ps | grep artheon-sast-backend >/dev/null 2>&1"

echo ""
echo -e "${BLUE}🌐 Verificando API...${NC}"
check "Health endpoint responde" "curl -s http://localhost:8000/health | grep 'healthy' >/dev/null 2>&1"
check "API está disponible en puerto 8000" "curl -s http://localhost:8000 | grep 'ARTHEON-SAST' >/dev/null 2>&1"

echo ""
echo -e "${BLUE}📋 Verificando contenido de archivos...${NC}"
check "main.py contiene FastAPI" "grep -q 'from fastapi import' artheon_backend/main.py"
check "language_analyzer.py contiene clase" "grep -q 'class LanguageAnalyzer' artheon_backend/language_analyzer.py"
check "requirements.txt contiene fastapi" "grep -q 'fastapi' artheon_backend/requirements.txt"
check "Dockerfile contiene python:3.11" "grep -q 'python:3.11' artheon_backend/Dockerfile"
check "docker-compose.yml contiene puerto 8000" "grep -q '8000' artheon_backend/docker-compose.yml"

echo ""
echo "=================================================="
echo -e "${YELLOW}Resultados: ${GREEN}$PASSED/${TOTAL}${NC} checks pasados"
echo "=================================================="

if [ $PASSED -eq $TOTAL ]; then
    echo -e "${GREEN}✓ Todo está correctamente configurado${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️  Algunos checks fallaron${NC}"
    exit 1
fi

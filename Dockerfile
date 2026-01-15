# Usar imagen oficial de Python
FROM python:3.11-slim

# Establecer directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Actualizar pip a la última versión
RUN pip install --upgrade pip setuptools wheel

# Copiar archivo de requisitos
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar - soporta puerto dinámico para Railway
CMD ["sh", "-c", "uvicorn src.artheon_sast.api.main:app --host 0.0.0.0 --port ${PORT:-8000}"]

# Comando para ejecutar la aplicación
CMD ["uvicorn", "src.artheon_sast.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]

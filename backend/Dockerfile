# Imagen base oficial de Python
FROM python:3.10-slim

# Configura el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Copia los archivos de requerimientos e instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Configura la variable de entorno FLASK_ENV
ENV FLASK_ENV=development
ENV PYTHONUNBUFFERED=1

# Puerto de exposición
EXPOSE 5000

# Comando predeterminado para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]

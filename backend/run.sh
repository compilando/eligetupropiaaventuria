#!/bin/bash

# Activar el entorno virtual si es necesario
if [ -f ".venv/bin/activate" ]; then	
    echo "Activando entorno virtual..."
    source .venv/bin/activate
else
    echo "No se encontró entorno virtual. Ejecutando sin activar entorno virtual."
fi

# Función para limpiar procesos al finalizar el script
cleanup() {
    echo "Cerrando la aplicación Flask..."
    if [[ -n "$FLASK_PID" ]] && ps -p $FLASK_PID > /dev/null; then
        kill $FLASK_PID
        wait $FLASK_PID 2>/dev/null
    fi
    exit
}

# Capturar señales para limpiar procesos
trap cleanup SIGINT SIGTERM

# Lanzar la aplicación Flask
echo "Iniciando la aplicación Flask..."
python run.py &

# Guardar el PID del proceso Flask
FLASK_PID=$!

# Esperar unos segundos para asegurarse de que el servidor esté en funcionamiento
sleep 8

# Abrir el navegador en la URL especificada
URL="http://127.0.0.1:5000/swagger/"
echo "Abriendo navegador en $URL"
xdg-open $URL || open $URL || echo "No se pudo abrir el navegador automáticamente. Accede manualmente a $URL"

# Esperar a que el proceso Flask termine
wait $FLASK_PID

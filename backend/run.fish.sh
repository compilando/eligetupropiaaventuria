#!/usr/bin/env fish

# Activar el entorno virtual si es necesario
if test -f ".venv/bin/activate"
    echo "Activando entorno virtual..."
    source .venv/bin/activate.fish
else
    echo "No se encontró entorno virtual. Ejecutando sin activar entorno virtual."
end

# Función para limpiar procesos al finalizar el script
function cleanup
    echo "Cerrando la aplicación Flask..."
    if test -n "$FLASK_PID" && ps -p $FLASK_PID > /dev/null
        kill $FLASK_PID
        wait $FLASK_PID ^/dev/null
    end
    exit
end

# Capturar señales para limpiar procesos
trap cleanup SIGINT SIGTERM

# Lanzar la aplicación Flask
echo "Iniciando la aplicación Flask..."
python run.py &

# Guardar el PID del proceso Flask
set -l FLASK_PID $last_pid

# Esperar unos segundos para asegurarse de que el servidor esté en funcionamiento
sleep 8

# Abrir el navegador en la URL especificada
set -l URL "http://127.0.0.1:5000/swagger/"
echo "Abriendo navegador en $URL"
xdg-open $URL; or open $URL; or echo "No se pudo abrir el navegador automáticamente. Accede manualmente a $URL"

# Esperar a que el proceso Flask termine
wait $FLASK_PID

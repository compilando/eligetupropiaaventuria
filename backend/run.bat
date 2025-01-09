@echo off
rem Activar el entorno virtual si es necesario
if exist .venv\Scripts\activate (
    echo Activando entorno virtual...
    call .venv\Scripts\activate
) else (
    echo No se encontró un entorno virtual. Ejecutando sin activar entorno virtual.
)

rem Iniciar la aplicación Flask
echo Iniciando la aplicación Flask...
start "" python run.py

rem Esperar unos segundos para asegurarse de que el servidor esté en funcionamiento
timeout /t 5 > nul

rem Abrir el navegador en la URL especificada
set URL=http://127.0.0.1:5000/swagger/
echo Abriendo navegador en %URL%
start %URL%

rem Mantener la ventana abierta hasta que el usuario la cierre
echo La aplicación Flask se está ejecutando. Presiona cualquier tecla para salir...
pause


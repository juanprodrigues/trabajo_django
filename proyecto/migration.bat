@echo off

REM Ejecutar general
py manage.py makemigrations
py manage.py migrate 

REM Ejecutar makemigrations
py manage.py makemigrations chat
py manage.py makemigrations servisarg

REM Ejecutar migrate

py manage.py migrate chat
py manage.py migrate servisarg

REM Pausa para ver los resultados
pause
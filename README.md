# Guía de Inicio Rápido para Bookland

Este repositorio contiene el código fuente para el proyecto Bookland, una aplicación web desarrollada con Django.

## Configuración Inicial

Para comenzar, sigue estos pasos:

1. Clona este repositorio en tu máquina local:

```bash
git clone https://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@github.com/Soel18/bookland.git

#con esto crea el proyecto de django
django-admin startproject bookland

#Con esto se inicializa el repositorio, solo esta vez se usará
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://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@github.com/Soel18/bookland.git

git push -u origin main

#con esto crea el entorno virtual
#python -m venv aquiponecomosevallamarelentorno
python -m venv myvenv

#pero antes de instalarl django activa el entorno virtual
source myvenv/Scripts/activate

#una vez creado el entorno instala django en su proyecto
pip install django==4.0

#ahora crearemos .gitignore para evitar subir el entorno virtual entre otras cosas que queramos
touch .gitignore

#ahora agregaremos los cambios que hemos hecho a github
git add .

#luego de hacer esto debemos siempre hacer un comentario de los cambios que hicimos
#git commit -m "UN MENSAJE"
git commit -m "Agrege .gitignore"

#ahora si podemos subir lo que hicimos a github
git push origin main

#aqui agregaremos readme.md para poner esta info

#para correr la app usamos esto
python manage.py runserver

#para apagarlo usamos 
ctrl+c
# Guía de Inicio Rápido para Bookland

Este repositorio contiene el código fuente para el proyecto Bookland, una aplicación web desarrollada con Django.

## Configuración Inicial

Para comenzar, sigue estos pasos:
1. Primero hay que crear una carpeta en el escritorio de la pc de cs50

2. Clonar el repositorio:
```bash
git clone https://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@github.com/Soel18/bookland.git
```

3. Crear el entorno virtual y activarlo
```bash
python -m venv myvenv
source myvenv/Scripts/activate
```

4. Instalar requerimientos
```bash
pip install -r requirements.txt
```
5. Para correr la app usamos esto
```bash
python manage.py runserver
#para apagarlo usamos ctrl+c
```

Si va subir los cambios a github:
## Los cambios, commit y los subiremos a github 
```bash
git add . #para agregar los cambios
git commit -m "Comentario" #para hacer un comentario de los cambios
git push origin main #para subirlo a github
```

Para crear el proyecto:
## YA NO ES NECESARIO HACERLO PORQUE EL PROYECTO YA ESTA CREADO
```bash
django-admin startproject bookland
```
## Con esto se inicializa el repositorio, solo esta vez se usará
```bash
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://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@github.com/Soel18/bookland.git
git push -u origin main
```
## Con esto crea el entorno virtual
```bash
python -m venv myvenv
```
## Con esto activa el entorno virtual
```bash
source myvenv/Scripts/activate
```

## Una vez creado el entorno instala django en su proyecto
```bash
pip install django==4.0
```

## Ahora crearemos .gitignore para evitar subir el entorno virtual entre otras cosas que queramos
```bash
touch .gitignore
```

## Ahora agregaremos los cambios, commit y los subiremos a github 
```bash
git add .
git commit -m "Agrege .gitignore"
git push origin main
```

## Para correr la app usamos esto
```bash
python manage.py runserver
#para apagarlo usamos ctrl+c
```



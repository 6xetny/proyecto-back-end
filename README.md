# Centro Médico Vida - Backend (appTurnos)

Este repositorio contiene el backend del sistema de agendamiento para el Centro Médico Vida, desarrollado con Django y Django Rest Framework utilizando Vistas Basadas en Clase (CBV).

## 👨‍💻 Autor
* Bastián

---

## 🚀 Cómo ejecutar este proyecto localmente

### 1. Preparar el entorno virtual
Abre la carpeta del proyecto en la terminal y crea/activa el entorno virtual:

    python -m venv ambiente
    .\ambiente\Scripts\Activate

### 2. Instalar dependencias
Instala todas las librerías necesarias preparadas en el proyecto:

    pip install -r requirements.txt

### 3. Configurar variables de entorno
Crea un archivo llamado .env en la raíz del proyecto (al mismo nivel que manage.py) y agrega la clave secreta de Django:

    SECRET_KEY='tu_clave_secreta_aqui'

### 4. Base de datos y Fixtures
Aplica las migraciones para construir las tablas en SQLite y carga los pacientes de prueba iniciales:

    python manage.py migrate
    python manage.py loaddata pacientes_iniciales.json

### 5. Crear usuario administrador
Para poder acceder al panel de control de Django (/admin/), crea un superusuario:

    python manage.py createsuperuser

### 6. Ejecutar el servidor
Finalmente, levanta el proyecto localmente:

    python manage.py runserver

* Sitio web (Frontend): http://127.0.0.1:8000/
* API Root (Backend): http://127.0.0.1:8000/api/

---

## 🛠️ Guía Rápida: Cómo crear un proyecto Django desde cero
*(Resumen de comandos base para futuros proyectos)*

1. Iniciar el entorno y el proyecto
* python -m venv ambiente ➡️ Crea el entorno virtual.
* .\ambiente\Scripts\Activate ➡️ Activa el entorno.
* pip install --upgrade pip ➡️ Actualiza el gestor de paquetes.
* pip install django djangorestframework python-decouple ➡️ Instala las herramientas clave.
* django-admin startproject motor_django . ➡️ Crea el proyecto base.
* django-admin startapp mi_aplicacion ➡️ Crea tu aplicación interna.

2. Base de Datos y Modelos
* python manage.py makemigrations ➡️ Traduce tus clases de models a SQL.
* python manage.py migrate ➡️ Ejecuta las instrucciones y crea las tablas.

3. Datos Iniciales y Administración
* python manage.py loaddata archivo.json ➡️ Carga datos precargados.
* python manage.py createsuperuser ➡️ Genera el acceso de administrador.

4. Buenas prácticas antes de entregar
* pip freeze > requirements.txt ➡️ Guarda la lista exacta de librerías.
# Centro Médico Vida - Backend (`appTurnos`)

Sistema de gestión y agendamiento de turnos médicos desarrollado con **Django**, **Django REST Framework** y **MySQL**, que combina una API REST mediante `ViewSet` con una interfaz web CRUD construida con **Vistas Basadas en Clase (CBV)** nativas, `ModelForm` y plantillas con **Bootstrap**.

## Autor
- Bastián

---

## Guía de Construcción y Ejecución del Proyecto

1. ## Creación de Ambiente Virtual
   - Habiendo clonado el repositorio del proyecto, abrimos la carpeta contenedora en **VS Code**.
   - Dentro de este directorio, crearemos un ambiente virtual que mantendrá aislada toda la configuración de nuestro proyecto y su entorno de trabajo.
   - Iniciamos un nuevo terminal estando ubicados en el directorio principal (`proyecto-back-end`) y ejecutamos:

     ```powershell
     python -m venv ambiente
     ```

   - *VENV* es acrónimo de *VIRTUAL ENVIRONMENT*, y crea el entorno aislado para nuestras dependencias.
   - *ambiente* es el nombre elegido para nuestro entorno virtual.
   - Este directorio contiene carpetas clave como:
     - *Lib*: Donde quedan instaladas las librerías del proyecto.
     - *Scripts*: Donde se encuentran los scripts para activar y desactivar el entorno.

2. ## Activación de Ambiente Virtual
   - Desde el terminal en la raíz del proyecto, activamos el entorno virtual ejecutando:

     ```powershell
     .\ambiente\Scripts\Activate.ps1
     ```

   - Si PowerShell bloquea la ejecución de scripts por políticas de seguridad, podemos usar `.\ambiente\Scripts\activate.bat` o ajustar la política de ejecución para el usuario actual:

     ```powershell
     Set-ExecutionPolicy Bypass -Scope CurrentUser
     ```

   - Una vez activado, veremos el prefijo `(ambiente)` en la terminal.
   - Cuando terminemos de trabajar o queramos salir del entorno virtual, ejecutamos:

     ```powershell
     deactivate
     ```

3. ## Actualización de PIP e Instalación de Dependencias
   - Con el entorno `(ambiente)` activado, actualizamos `pip` para evitar problemas con versiones antiguas:

     ```powershell
     python -m pip install --upgrade pip
     ```

   - Instalamos todas las dependencias del proyecto desde `requirements.txt` (incluyendo Django, Django REST Framework, `python-decouple` y el driver de MySQL):

     ```powershell
     pip install -r requirements.txt
     ```

   - Si se instala una librería nueva durante el desarrollo, respaldamos el entorno con:

     ```powershell
     pip freeze > requirements.txt
     ```

4. ## Desacoplar Datos Sensibles y Configurar MySQL
   - Para no dejar credenciales ni claves sensibles dentro del código, usamos `python-decouple` y un archivo `.env` en la raíz del proyecto (al mismo nivel que `manage.py`).
   - Verificamos que el servicio de **MySQL** esté iniciado en el equipo y creamos la base de datos y el usuario correspondiente:

     ```sql
     CREATE DATABASE IF NOT EXISTS centro_medico CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     CREATE USER IF NOT EXISTS 'admin_vida'@'localhost' IDENTIFIED BY 'Vida2026*';
     GRANT ALL PRIVILEGES ON centro_medico.* TO 'admin_vida'@'localhost';
     FLUSH PRIVILEGES;
     ```

   - En el archivo `.env` definimos las variables del proyecto:

     ```env
     SECRET_KEY='tu_clave_secreta_aqui'
     DB_NAME=centro_medico
     DB_USER=admin_vida
     DB_PASSWORD=Vida2026*
     DB_HOST=localhost
     DB_PORT=3306
     ```

   - En `django_turnos/settings.py` configuramos `DATABASES` para conectarnos a MySQL leyendo estas variables mediante `config(...)`:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': config('DB_NAME'),
             'USER': config('DB_USER'),
             'PASSWORD': config('DB_PASSWORD'),
             'HOST': config('DB_HOST'),
             'PORT': config('DB_PORT'),
         }
     }
     ```

5. ## Modelo de Datos y Migraciones
   - Registramos `'rest_framework'` y `'appTurnos'` en `INSTALLED_APPS` dentro de `django_turnos/settings.py`.
   - En `appTurnos/models.py` definimos las clases que heredan de `models.Model` y representan las tablas en MySQL mediante el ORM de Django:
     - `Especialista`: `rut` (`unique=True`), `nombre`, `apellido`, `especialidad`, `activo`, `created_at` (`auto_now_add=True`) y `updated_at` (`auto_now=True`)[cite: 1].
     - `Paciente`: `rut` (`unique=True`), `nombre`, `apellido`, `email`, `telefono`, `fecha_nacimiento`, `activo`, `created_at` y `updated_at`[cite: 1].
     - `Turno`: relaciones `ForeignKey` hacia `Especialista` y `Paciente` (`on_delete=models.CASCADE`), `fecha`, `hora`, `estado` con `choices` (`Pendiente`, `Confirmado`, `Cancelado`, `Completado`), `observaciones`, `created_at` y `updated_at`[cite: 1, 2].
   - Generamos y aplicamos las migraciones en MySQL:

     ```powershell
     python manage.py makemigrations
     python manage.py migrate
     ```

   - Si contamos con fixtures en `appTurnos/fixtures/` (como `pacientes_iniciales.json`), podemos cargarlos con:

     ```powershell
     python manage.py loaddata pacientes_iniciales.json
     ```

   - Para acceder al panel administrativo en `/admin/`, creamos un superusuario:

     ```powershell
     python manage.py createsuperuser
     ```

6. ## Serializadores, API REST (`ViewSet`) y Rutas
   - En `appTurnos/serializers.py` definimos los `ModelSerializer` (`EspecialistaSerializer`, `PacienteSerializer`, `TurnoSerializer`).
   - En `appTurnos/views.py` registramos los `ModelViewSet` (`EspecialistaViewSet`, `PacienteViewSet`, `TurnoViewSet`)[cite: 3].
   - En `appTurnos/urls.py` configuramos `routers.DefaultRouter()` para exponer los endpoints de la API REST, y en `django_turnos/urls.py` incluimos `appTurnos.urls` bajo `api/` junto con la ruta raíz y `/admin/`[cite: 4, 6].

7. ## CRUD Manual con CBV, Formularios (`ModelForm`) y Plantillas
   - Además de los `ViewSet` de DRF, implementamos vistas tradicionales con **CBV nativas** (`TemplateView`, `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`) para que los usuarios gestionen los registros desde el navegador con validaciones de formulario[cite: 18, 19].
   - En `appTurnos/forms.py` creamos `EspecialistaForm`, `PacienteForm` y `TurnoForm` heredando de `forms.ModelForm`, asignando clases y widgets de Bootstrap (`form-control`, `form-select`, `form-check-input`, `date`, `time`, `Textarea`)[cite: 19].
   - En `appTurnos/templates/appTurnos/` creamos las plantillas HTML (`base.html`, `bienvenida.html`, `form_generico.html`, `confirmar_eliminar.html`, además de los listados y detalles de `especialista`, `paciente` y `turno`)[cite: 9].

8. ## Ejecución del Servidor y Rutas Principales
   - Con todo configurado, levantamos el servidor de desarrollo:

     ```powershell
     python manage.py runserver
     ```

   - Rutas disponibles al ejecutar localmente:
     - **Bienvenida:** `http://127.0.0.1:8000/`[cite: 6, 16]
     - **Pacientes (Web CBV):** `http://127.0.0.1:8000/api/web/pacientes/`
     - **Especialistas (Web CBV):** `http://127.0.0.1:8000/api/web/especialistas/`[cite: 17, 18]
     - **Turnos (Web CBV):** `http://127.0.0.1:8000/api/web/turnos/`
     - **API REST (DRF):** `http://127.0.0.1:8000/api/`[cite: 6]
     - **Administrador Django:** `http://127.0.0.1:8000/admin/`[cite: 6]
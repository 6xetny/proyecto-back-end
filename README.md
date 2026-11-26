# Centro Médico Vida - Backend (`appTurnos`)

## Desarrollo de Backend con Django y DRF

Como desarrollador del proyecto, he estructurado este repositorio para implementar el sistema de gestión y agendamiento de turnos médicos del **Centro Médico Vida** utilizando **Django**, **Django REST Framework**, **MySQL** y **Vistas Basadas en Clase (CBV)**.

- Este proyecto corresponde a la aplicación `appTurnos` dentro del proyecto `django_turnos`, conectada a una base de datos MySQL y con variables sensibles desacopladas mediante `.env`.
- En el código conviven los endpoints de la API REST (`ViewSet`) y el CRUD web manual construido con CBV nativas, `ModelForm` y plantillas con Bootstrap.

## Creación del Proyecto con Django

1. ## Creación de Ambiente Virtual
   - Habiendo clonado el repositorio del proyecto, abrimos la carpeta contenedora en **VS Code**.
   - Dentro de este directorio, crearemos un ambiente virtual que mantendrá aislada toda la configuración de nuestro proyecto y su entorno de trabajo.
   - Para lograrlo, iniciaremos un nuevo terminal, estando ubicados en el directorio principal (`proyecto-back-end`) y ejecutamos:

     ```powershell
     python -m venv ambiente
     ```

   - *VENV* es acrónimo de *VIRTUAL ENVIRONMENT*, por lo que debemos entender que creará nuestro ambiente virtual.
   - *ambiente* es el nombre que elegí para mi ambiente virtual.
   - Este directorio contiene carpetas clave como:
     - *Lib*: Donde encontraremos las librerías asociadas a nuestro proyecto.
     - *Scripts*: Donde se encuentran los scripts para activar y desactivar el entorno, como `Activate` y `deactivate`.

2. ## Activación de Ambiente Virtual
   - Desde el terminal en la raíz del proyecto, activamos el entorno virtual ejecutando:

     ```powershell
     .\ambiente\Scripts\Activate.ps1
     ```

   - Si no se puede ejecutar el comando por restricciones de seguridad en PowerShell, debemos darle permisos al terminal o usar el script `.bat`:

     ```powershell
     Set-ExecutionPolicy Bypass -Scope CurrentUser
     ```

   - Una vez activado, veremos `(ambiente)` al inicio de la línea en la terminal.
   - Si hemos terminado de trabajar o debemos cambiarnos de proyecto, necesitamos desactivar el ambiente virtual con:

     ```powershell
     deactivate
     ```

3. ## Actualización de PIP e Instalación de Dependencias
   - A pesar de haber generado una instalación del entorno desde cero, no está asegurado que contenga la última versión de `pip`, por lo que debemos actualizarlo:

     ```powershell
     python -m pip install --upgrade pip
     ```

   - Luego instalamos las dependencias del proyecto desde `requirements.txt` (incluyendo Django, `djangorestframework`, `python-decouple` y el driver de MySQL):

     ```powershell
     pip install -r requirements.txt
     ```

   - Cuando agregamos una librería nueva durante el desarrollo, respaldamos las dependencias con:

     ```powershell
     pip freeze > requirements.txt
     ```

4. ## Desacoplar Datos Sensibles y Configurar Base de Datos MySQL
   - Para trabajar con una base de datos externa sin exponer credenciales ni la `SECRET_KEY` en el código, desacoplamos los datos sensibles usando `python-decouple` y un archivo `.env` en la raíz del proyecto (al mismo nivel que `manage.py`).
   - Primero aseguramos que el servicio de **MySQL** esté activo en el equipo y creamos la base de datos y el usuario con sus permisos:

     ```sql
     CREATE DATABASE IF NOT EXISTS centro_medico CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     CREATE USER IF NOT EXISTS 'admin_vida'@'localhost' IDENTIFIED BY 'Vida2026*';
     GRANT ALL PRIVILEGES ON centro_medico.* TO 'admin_vida'@'localhost';
     FLUSH PRIVILEGES;
     ```

   - Creamos el archivo `.env` en la raíz del proyecto sin dejar espacios alrededor del signo `=`:

     ```env
     SECRET_KEY='tu_clave_secreta_aqui'
     DB_NAME=centro_medico
     DB_USER=admin_vida
     DB_PASSWORD=Vida2026*
     DB_HOST=localhost
     DB_PORT=3306
     ```

   - En `django_turnos/settings.py` importamos `config` desde `decouple` y configuramos `DATABASES` para usar MySQL en lugar de SQLite:

     ```python
     from decouple import config

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
   - Registramos `'rest_framework'` y `'appTurnos'` dentro de `INSTALLED_APPS` en `django_turnos/settings.py`.
   - En `appTurnos/models.py` definimos las clases que heredan de `models.Model` y que el ORM de Django mapea a tablas en MySQL:
     - `Especialista`: `rut` (`unique=True`), `nombre`, `apellido`, `especialidad`, `activo`, `created_at` (`auto_now_add=True`) y `updated_at` (`auto_now=True`).
     - `Paciente`: `rut` (`unique=True`), `nombre`, `apellido`, `email`, `telefono`, `fecha_nacimiento`, `activo`, `created_at` y `updated_at`.
     - `Turno`: relaciones `ForeignKey` hacia `Especialista` y `Paciente` (`on_delete=models.CASCADE`), `fecha`, `hora`, `estado` con `choices` (`Pendiente`, `Confirmado`, `Cancelado`, `Completado`), `observaciones`, `created_at` y `updated_at`.
   - Generamos y aplicamos las migraciones en la base de datos:

     ```powershell
     python manage.py makemigrations
     python manage.py migrate
     ```

   - Cada vez que modificamos los modelos, volvemos a ejecutar `makemigrations` y `migrate` para mantener sincronizada la estructura en MySQL.

6. ## Datos Iniciales (Fixtures) y Panel Administrador
   - En `appTurnos/fixtures/` podemos alojar archivos `.json` con datos iniciales y cargarlos con:

     ```powershell
     python manage.py loaddata pacientes_iniciales.json
     ```

   - En `appTurnos/admin.py` registramos los modelos (`Especialista`, `Paciente`, `Turno`) y creamos un superusuario para acceder a `/admin/`:

     ```powershell
     python manage.py createsuperuser
     ```

7. ## Serializadores, API REST (`ViewSet`) y Rutas
   - En `appTurnos/serializers.py` creamos los `ModelSerializer` (`EspecialistaSerializer`, `PacienteSerializer`, `TurnoSerializer`) para serializar los objetos en JSON.
   - En `appTurnos/views.py` definimos los `ModelViewSet` (`EspecialistaViewSet`, `PacienteViewSet`, `TurnoViewSet`) para las operaciones REST.
   - En `appTurnos/urls.py` registramos los ViewSets en `routers.DefaultRouter()` y exponemos las rutas del enrutador.
   - En `django_turnos/urls.py` incluimos `appTurnos.urls` bajo la ruta `api/`, junto con la ruta principal y `/admin/`.

8. ## CRUD Manual con CBV, Formularios (`ModelForm`) y Plantillas
   - Además de los `ViewSet` de DRF, implementamos el CRUD web tradicional utilizando **Vistas Basadas en Clase (CBV)** nativas de Django y formularios `ModelForm` con widgets de Bootstrap (`form-control`, `form-select`, `form-check-input`, `date`, `time`, `Textarea`) en `appTurnos/forms.py`.
   - En `appTurnos/templates/appTurnos/` creamos las plantillas HTML (`base.html`, `bienvenida.html`, `form_generico.html`, `confirmar_eliminar.html` y las vistas de listado y detalle para cada entidad).
   - **Cobertura obligatoria de CBV por entidad principal:** Todas las entidades principales del modelo de datos (`Especialista`, `Paciente` y `Turno`) cuentan de forma obligatoria y funcional con sus cinco vistas CBV implementadas en `appTurnos/views.py` y conectadas en `appTurnos/urls.py`:
     - **Especialista:** `EspecialistaListView`, `EspecialistaDetailView`, `EspecialistaCreateView`, `EspecialistaUpdateView` y `EspecialistaDeleteView`.
     - **Paciente:** `PacienteListView`, `PacienteDetailView`, `PacienteCreateView`, `PacienteUpdateView` y `PacienteDeleteView`.
     - **Turno:** `TurnoListView`, `TurnoDetailView`, `TurnoCreateView`, `TurnoUpdateView` y `TurnoDeleteView`.
   - **Justificación de omisión de vistas:** No se omite ninguna de las cinco vistas CBV (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`) en ninguna de las entidades principales (`Especialista`, `Paciente` o `Turno`), ya que todas son necesarias para listar, consultar el detalle, crear, editar y eliminar registros desde la interfaz web. (`BienvenidaView` hereda de `TemplateView` como vista pública de entrada).

9. ## Ejecución del Servidor y Rutas de Acceso
   - Iniciamos el servidor de desarrollo con:

     ```powershell
     python manage.py runserver
     ```

   - URLs principales disponibles en ejecución local:
     - **Bienvenida:** `http://127.0.0.1:8000/`
     - **Pacientes (CRUD CBV):** `http://127.0.0.1:8000/api/web/pacientes/`
     - **Especialistas (CRUD CBV):** `http://127.0.0.1:8000/api/web/especialistas/`
     - **Turnos (CRUD CBV):** `http://127.0.0.1:8000/api/web/turnos/`
     - **API REST (DRF):** `http://127.0.0.1:8000/api/`
     - **Administrador Django:** `http://127.0.0.1:8000/admin/`
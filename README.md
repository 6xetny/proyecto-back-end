
# Proyectos Backend con Django

## Instrucciones de Instalación y Ejecución

### 1. Crear el Ambiente Virtual
 Abre un terminal en el directorio de tu proyecto y ejecuta el siguiente comando para crear el ambiente aislado:

 ```
 python -m venv ambiente
 ```

2. **Activación del Ambiente Virtual.**
    Activar el Ambiente Virtual
    Navega al subdirectorio Scripts dentro del ambiente creado y actívalo:
    - Mediante el terminal nos ubicamos dentro del directorio creado con la instrucción anterior.
    - Dentro de este directorio, nos movemos al subdirectorio Scripts.
    - Dentro de Scripts, ejecutamos el siguiente comando en nuestro terminal:

    ```
    .\Activate
    ```
    - Si obtienes un error de permisos en el terminal, ejecuta esta instrucción y vuelve a intentar la activación:

    ```
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

    - Si trabajamos en varios proyectos y debemos cambiar de un ambiente a otro, desactivaremos el ambiente con el siguiente comando:

    ```
    deactivate
   ```

3. **Instalar Dependencias**
    Con el ambiente activo, instala las dependencias necesarias:

    ```
    pip install django
    ```
    - Ahora que las dependencias de Django ya han sido instaladas, crearemos nuestro primer proyecto Django, ejecutando el siguiente comando:
    ```
    django-admin startproject nombre_django .
    ```
    - nombre_django debe ser reemplazado por el nombre que Ud. le dará a su motor Django, es común que se use el acrónimo drf (Django 
    Rest framework). Idealmente debe ser un nombre corto, porque deberemos llamarlo en más de alguna oportunidad.

4. **Creación de Aplicación**
    - Cuando ya tenemos un motor Django funcional, podemos crear nuestra aplicación particular que contendrá los controladores, las vistas y los modelos.
    - Para crear nuestra aplicación, nos ubicamos mediante el terminal en la carpeta raíz del proyecto y ejecutamos el siguiente comando:
    ```
    django-admin startapp nombre_aplicacion
    ```
    - nombre_aplicacion debe ser reemplazado por el nombre que Ud. le dará a su aplicación, el que debe ser descriptivo para seguir normativas de buenas prácticas.
    - Una vez creada la aplicación, debemnos agregar el nombre de la aplicación a la lista de INSTALLED_APPS de setting.py de nuestro núcleo django.
    - Ya creada la aplicación, iniciamos el servidor para confirmar que todo está funcionando OK.
    - El servidor se inicia con el siguiente comando mediante terminal:
    ```
    python manage.py runserver
    ```
    - Si todo ha funcionado de manera correcta, debiera cargar una vista genérica de Django al iniciar el servidor.


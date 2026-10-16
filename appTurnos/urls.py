from django.urls import path, include
from rest_framework import routers
from . import views

# 1. Creamos el enrutador
enrutador = routers.DefaultRouter()

# 2. Registramos nuestras Vistas Basadas en Clase
enrutador.register(r'pacientes', views.PacienteViewSet)
enrutador.register(r'especialistas', views.EspecialistaViewSet)
enrutador.register(r'turnos', views.TurnoViewSet)

# 3. Exponemos las rutas autogeneradas
urlpatterns = [
    path('', include(enrutador.urls))
]
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Especialista, Paciente, Turno

# Registramos los modelos para que aparezcan en el panel de administración
admin.site.register(Especialista)
admin.site.register(Paciente)
admin.site.register(Turno)
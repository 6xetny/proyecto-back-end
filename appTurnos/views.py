from django.shortcuts import render
from rest_framework import viewsets

# Importamos los modelos
from .models import Paciente, Especialista, Turno

# Importamos los serializadores
from .serializers import PacienteSerializer, EspecialistaSerializer, TurnoSerializer

# ==========================================
# VISTAS WEB (FRONTEND HTML)
# ==========================================
def inicio(request):
    return render(request, 'turnos/index.html')

def agendar_turno(request):
    return render(request, 'turnos/agendar.html')

# ==========================================
# VISTAS DE API (BACKEND CBV - VIEWSETS)
# ==========================================
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class EspecialistaViewSet(viewsets.ModelViewSet):
    queryset = Especialista.objects.all()
    serializer_class = EspecialistaSerializer

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
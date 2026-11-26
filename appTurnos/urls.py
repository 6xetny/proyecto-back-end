from django.urls import path, include
from rest_framework import routers
from . import views

# 1. Enrutador API REST 
enrutador = routers.DefaultRouter()
enrutador.register(r'pacientes', views.PacienteViewSet)
enrutador.register(r'especialistas', views.EspecialistaViewSet)
enrutador.register(r'turnos', views.TurnoViewSet)

# 2. Rutas CBV Web
urlpatterns = [
    path('', include(enrutador.urls)),
    path('bienvenida/', views.BienvenidaView.as_view(), name='bienvenida'),

    # Pacientes
    path('web/pacientes/', views.PacienteListView.as_view(), name='paciente_list'),
    path('web/pacientes/<int:pk>/', views.PacienteDetailView.as_view(), name='paciente_detail'),
    path('web/pacientes/nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('web/pacientes/<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('web/pacientes/<int:pk>/eliminar/', views.PacienteDeleteView.as_view(), name='paciente_delete'),

    # Especialistas
    path('web/especialistas/', views.EspecialistaListView.as_view(), name='especialista_list'),
    path('web/especialistas/<int:pk>/', views.EspecialistaDetailView.as_view(), name='especialista_detail'),
    path('web/especialistas/nuevo/', views.EspecialistaCreateView.as_view(), name='especialista_create'),
    path('web/especialistas/<int:pk>/editar/', views.EspecialistaUpdateView.as_view(), name='especialista_update'),
    path('web/especialistas/<int:pk>/eliminar/', views.EspecialistaDeleteView.as_view(), name='especialista_delete'),

    # Turnos
    path('web/turnos/', views.TurnoListView.as_view(), name='turno_list'),
    path('web/turnos/<int:pk>/', views.TurnoDetailView.as_view(), name='turno_detail'),
    path('web/turnos/nuevo/', views.TurnoCreateView.as_view(), name='turno_create'),
    path('web/turnos/<int:pk>/editar/', views.TurnoUpdateView.as_view(), name='turno_update'),
    path('web/turnos/<int:pk>/eliminar/', views.TurnoDeleteView.as_view(), name='turno_delete'),
]
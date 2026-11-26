from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .models import Paciente, Especialista, Turno
from .serializers import PacienteSerializer, EspecialistaSerializer, TurnoSerializer
from .forms import PacienteForm, EspecialistaForm, TurnoForm


# ==========================================
# VISTA PÚBLICA DE BIENVENIDA Y VISTAS WEB
# ==========================================
class BienvenidaView(TemplateView):
    template_name = 'appTurnos/bienvenida.html'


def inicio(request):
    return render(request, 'turnos/index.html')


def agendar_turno(request):
    return render(request, 'turnos/agendar.html')


# ==========================================
# CRUD WEB CON CBV - PACIENTES
# ==========================================
class PacienteListView(ListView):
    model = Paciente
    template_name = 'appTurnos/paciente_list.html'
    context_object_name = 'pacientes'


class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'appTurnos/paciente_detail.html'
    context_object_name = 'paciente'


class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'appTurnos/form_generico.html'
    success_url = reverse_lazy('paciente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Paciente'
        context['url_volver'] = reverse_lazy('paciente_list')
        return context


class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'appTurnos/form_generico.html'
    success_url = reverse_lazy('paciente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Paciente'
        context['url_volver'] = reverse_lazy('paciente_list')
        return context


class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'appTurnos/confirmar_eliminar.html'
    context_object_name = 'objeto'
    success_url = reverse_lazy('paciente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Paciente'
        context['url_volver'] = reverse_lazy('paciente_list')
        return context


# ==========================================
# CRUD WEB CON CBV - ESPECIALISTAS
# ==========================================
class EspecialistaListView(ListView):
    model = Especialista
    template_name = 'appTurnos/especialista_list.html'
    context_object_name = 'especialistas'


class EspecialistaDetailView(DetailView):
    model = Especialista
    template_name = 'appTurnos/especialista_detail.html'
    context_object_name = 'especialista'


class EspecialistaCreateView(CreateView):
    model = Especialista
    form_class = EspecialistaForm
    template_name = 'appTurnos/form_generico.html'
    success_url = reverse_lazy('especialista_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Especialista'
        context['url_volver'] = reverse_lazy('especialista_list')
        return context


class EspecialistaUpdateView(UpdateView):
    model = Especialista
    form_class = EspecialistaForm
    template_name = 'appTurnos/form_generico.html'
    success_url = reverse_lazy('especialista_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Especialista'
        context['url_volver'] = reverse_lazy('especialista_list')
        return context


class EspecialistaDeleteView(DeleteView):
    model = Especialista
    template_name = 'appTurnos/confirmar_eliminar.html'
    context_object_name = 'objeto'
    success_url = reverse_lazy('especialista_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Especialista'
        context['url_volver'] = reverse_lazy('especialista_list')
        return context


# ==========================================
# CRUD WEB CON CBV - TURNOS
# ==========================================
class TurnoListView(ListView):
    model = Turno
    template_name = 'appTurnos/turno_list.html'
    context_object_name = 'turnos'


class TurnoDetailView(DetailView):
    model = Turno
    template_name = 'appTurnos/turno_detail.html'
    context_object_name = 'turno'


class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'appTurnos/form_generico.html'
    success_url = reverse_lazy('turno_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Turno'
        context['url_volver'] = reverse_lazy('turno_list')
        return context


class TurnoUpdateView(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'appTurnos/form_generico.html'
    success_url = reverse_lazy('turno_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Turno'
        context['url_volver'] = reverse_lazy('turno_list')
        return context


class TurnoDeleteView(DeleteView):
    model = Turno
    template_name = 'appTurnos/confirmar_eliminar.html'
    context_object_name = 'objeto'
    success_url = reverse_lazy('turno_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Turno'
        context['url_volver'] = reverse_lazy('turno_list')
        return context


# ==========================================
# VISTAS DE API (DJANGO REST FRAMEWORK)
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
from django import forms
from .models import Especialista, Paciente, Turno


class EspecialistaForm(forms.ModelForm):
    class Meta:
        model = Especialista
        fields = ['rut', 'nombre', 'apellido', 'especialidad', 'activo']
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 12345678-9',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del especialista',
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido del especialista',
            }),
            'especialidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Medicina General, Kinesiología',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'rut',
            'nombre',
            'apellido',
            'email',
            'telefono',
            'fecha_nacimiento',
            'activo',
        ]
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 11222333-4',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del paciente',
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido del paciente',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: +56912345678',
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = [
            'especialista',
            'paciente',
            'fecha',
            'hora',
            'estado',
            'observaciones',
        ]
        widgets = {
            'especialista': forms.Select(attrs={
                'class': 'form-select',
            }),
            'paciente': forms.Select(attrs={
                'class': 'form-select',
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'hora': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select',
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Motivo de consulta o indicaciones (opcional)',
            }),
        }
#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import trabajadores

class trabajadoresForm(forms.ModelForm):
    cedulatr = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Cedula de Trabajador'}))
    nombretr = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Nombre de Trabajador'}))
    apellstr = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Apellidos de Trabajador'}))
    teltr = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Telefono de Trabajador'}))
    direcciontr = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Direccion de Trabajador'}))
    tipoacc = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Tipo de Acceso de Trabajador'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Contraseña de Acceso de Trabajador'}))

    class Meta:
        model = trabajadores
        fields = ['cedulatr', 'nombretr', 'apellstr', 'teltr', 'direcciontr', 'tipoacc', 'password']

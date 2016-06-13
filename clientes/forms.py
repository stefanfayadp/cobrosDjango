#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import clientes

class clientesForm(forms.ModelForm):
    cedula = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Cedula de Cliente'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Nombre de Cliente'}))
    apells = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Apellidos de Cliente'}))
    tel = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Telefono de Cliente'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Direccion de Cliente'}))

    class Meta:
        model = clientes
        fields = ['cedula', 'nombre', 'apells', 'tel', 'direccion']

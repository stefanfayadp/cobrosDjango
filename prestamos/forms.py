#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import prestamos
from clientes.models import clientes
from trabajadores.models import trabajadores

class prestamosForm(forms.ModelForm):
    idTrabajador = forms.ModelChoiceField(queryset = trabajadores.objects.all())
    cedula = forms.ModelChoiceField(queryset = clientes.objects.all())
    monto = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Monto del Prestamo'}))
    numdias = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Numero de dias del Prestamo'}))
    valordiaro = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese valor diario del Prestamo'}))
    fechainicio = forms.DateField(widget=forms.SelectDateWidget())
    fechafin = forms.DateField(widget=forms.SelectDateWidget())
    estado = forms.CharField(widget=forms.TextInput(attrs={'class': 'error', 'placeholder': 'Ingrese Estado del Prestamo'}))

    class Meta:
        model = prestamos
        fields = ['idTrabajador', 'cedula', 'monto', 'numdias', 'valordiario', 'fechainicio', 'fechafin', 'estado']

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import prestamos
from clientes.models import clientes
from trabajadores.models import trabajadores
from .forms import prestamosForm

def inicio(request):
    Prestamos = prestamos.objects.all()
    Trabajadores = trabajadores.objects.all()
    Clientes = clientes.objects.all()
    return render(request, 'inicio.html', {'Prestamos':Prestamos, 'Trabajadores': Trabajadores, 'Clientes': Clientes })

def prestamosCreation(request, template='prestamosForm.html'):
    form = prestamosForm()
    if request.method == "POST":
        form = prestamosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'prestamosNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))


def prestamosList(request):
    Prestamos = prestamos.objects.all()
    return render(request, 'prestamosListado.html', {'Prestamos': Prestamos})

def prestamosDetail(request, idPrestamo, template='prestamosDetalle.html'):
    Prestamos = get_object_or_404(prestamos, pk=idPrestamo)
    return render_to_response(template, {'Prestamos':Prestamos}, context_instance=RequestContext(request))

def prestamosDelete(request, id_idPrestamo):
    instance = get_object_or_404(prestamos, idPrestamo = id_idPrestamo)
    instance.delete()
    Prestamos = prestamos.objects.all()
    return render(request, 'prestamosListado.html', {'Prestamos': Prestamos})

def prestamosUpdate(request, id_idPrestamo):
    instance = get_object_or_404(prestamos,  idPrestamo = id_idPrestamo)
    form = prestamosForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            Prestamos = prestamos.objects.all()
            return render(request, 'prestamosListado.html', {'Prestamos': Prestamos})
    return render(request, 'prestamosDetalle.html', {'form':form})

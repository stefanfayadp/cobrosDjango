from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import trabajadores
from clientes.models import clientes
from prestamos.models import prestamos
from .forms import trabajadoresForm

def inicio(request):
    Trabajadores = trabajadores.objects.all()
    Clientes = clientes.objects.all()
    Prestamos = prestamos.objects.all()
    return render(request, 'inicio.html', {'Trabajadores': Trabajadores, 'Clientes': Clientes, 'Prestamos':Prestamos})

def trabajadoresCreation(request, template='trabajadoresForm.html'):
    form = trabajadoresForm()
    if request.method == "POST":
        form = trabajadoresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'trabajadoresNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def trabajadoresList(request):
    Trabajadores = trabajadores.objects.all()
    return render(request, 'trabajadoresListado.html', {'Trabajadores': Trabajadores})

def trabajadoresDetail(request, idtrabajador, template='trabajadoresDetalle.html'):
    Trabajadores = get_object_or_404(trabajadores, pk=idTrabajador)
    return render_to_response(template, {'Trabajadores':Trabajadores}, context_instance=RequestContext(request))

def trabajadoresDelete(request, id_idTrabajador):
    instance = get_object_or_404(trabajadores, idTrabajador = id_idTrabajador)
    instance.delete()
    Trabajadores = trabajadores.objects.all()
    return render(request, 'trabajadoresListado.html', {'Trabajadores': Trabajadores})

def trabajadoresUpdate(request, id_idTrabajador):
    instance = get_object_or_404(trabajadores,  idTrabajador = id_idTrabajador)
    form = trabajadoresForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            Trabajadores = trabajadores.objects.all()
            return render(request, 'trabajadoresListado.html', {'Trabajadores': Trabajadores})
    return render(request, 'trabajadoresDetalle.html', {'form':form})

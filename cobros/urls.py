"""cobros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'clientes.views.inicio', name='inicio'),
    url(r'^clientes/nuevo/$','clientes.views.clientesCreation', name='clientes_nuevo'),
    url(r'^clientes/listado/$','clientes.views.clientesList', name='clientes_listado'),
    url(r'^clientes/(?P<id_cedula>\d+)$','clientes.views.clientesUpdate', name='clientes_detalle'),
    url(r'^clientes_e/(?P<id_cedula>\d+)$','clientes.views.clientesDelete', name='clientes_borrar'),
    url(r'^trabajadores/nuevo/$','trabajadores.views.trabajadoresCreation', name='trabajadores_nuevo'),
    url(r'^trabajadores/listado/$','trabajadores.views.trabajadoresList', name='trabajadores_listado'),
    url(r'^trabajadores/(?P<id_idTrabajador>\d+)$','trabajadores.views.trabajadoresUpdate', name='trabajadores_detalle'),
    url(r'^trabajadores_e/(?P<id_idTrabajador>\d+)$','trabajadores.views.trabajadoresDelete', name='trabajadores_borrar'),
    url(r'^prestamos/nuevo/$','prestamos.views.prestamosCreation', name='prestamos_nuevo'),
    url(r'^prestamos/listado/$','prestamos.views.prestamosList', name='prestamos_listado'),
    url(r'^prestamos/(?P<id_idPrestamo>\d+)$','prestamos.views.prestamosUpdate', name='prestamos_detalle'),
    url(r'^prestamos_e/(?P<id_idPrestamo>\d+)$','prestamos.views.prestamosDelete', name='prestamos_borrar'),
)

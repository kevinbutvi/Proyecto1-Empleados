from dataclasses import fields
from multiprocessing import context
from operator import mod
from sre_constants import SUCCESS
from statistics import mode

from applications.departamento.models import Departamento
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView)

# Forms
from .forms import EmpleadoForm
# Models
from .models import Empleado

# DOCUMENTACION DE VISTAS GENERICAS
# https://ccbv.co.uk/

# TEMPLATE VIEW
class Pruebaview(TemplateView):
    """ Vista a pagina de prueba

    Args:
        TemplateView ():
    """
    template_name = "home/persona.html"


class ListAllEmpleados(ListView):
    """ Vista que muestra empleados por filtro de full_name

    Args:
        full_name

    Returns:
        empleados (object), con pagination
    """
    template_name = "persona/list_all.html"
    paginate_by = 4
    # Al usar paginacion, automaticamente se crea un objeto llamado "page_obj" que sirve para identificar los numeros de pagina y navegar
    ordering = "id"
    context_object_name = "empleados"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword1",'')
        lista = Empleado.objects.filter(full_name__icontains=palabra_clave)
        return lista


class ListAllEmpleadosAdmin(ListView):
    """ Vista que muestra todos los empleados y permite edicion 

    Returns:
        empleados (object), con pagination
    """
    template_name = "persona/lista_empleados.html"
    paginate_by = 4
    ordering = "id"
    context_object_name = "empleados"
    model = Empleado


class ListByAreaEmpleado(ListView):
    """ Vista que muestra empleados segun departamento

    Args:
        area

    Returns:
        empleados (object), con pagination
    """
    template_name = "persona/list_filtro.html"

    def get_queryset(self):
        area = self.kwargs['shotname']
        queryset = Empleado.objects.filter(departamento__shot_name = area)
        return queryset

    context_object_name = "empleados"


class ListEmpleadoByKword(ListView):
    """ Vista que muestro empleado particular por nombre

    Args:
        first_name

    Returns:
        empleados (object)
    """
    template_name = "persona/by_kword.html"
    context_object_name = "empleados"
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword1",'')
        lista = Empleado.objects.filter(first_name = palabra_clave)
        return lista


# DETAIL VIEW
class EmpleadoDetailView(DetailView):
    """ Vista que muestra detalle de empleado segun PK

    Args:
        pk = ID

    Returns:
        emple (object)
    """
    model = Empleado
    template_name = "persona/detail_empleado.html"
    context_object_name = "emple"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = "EL TITULO QUE ASIGNE SOBREESCRIBIENDO"
        return context


# TEMPLATE VIEW 
class SuccesView(TemplateView):
    """ Vista de Exito"""
    template_name = "persona/success.html"


# CREATE VIEW
class EmpleadoCreateView(CreateView):
    """ Vista para registrar nuevo empleado """
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy("persona_app:empleados_admin")
    
    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


# UPDATE VIEW
class EmpleadoUpdateView(UpdateView):
    """ Vista para actualizar datos de un empleado en particular """
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        "first_name",
        "last_name",
        "job",
        "departamento",
        "habilidades",
    ]
    success_url = reverse_lazy("persona_app:empleados_admin")
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


# DELETE VIEW 
class EmpleadoDeleteView(DeleteView):
    """ Vista para eliminar empleado """
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy("persona_app:empleados_admin")
    object_context_name = "empleado"


class InicioView(TemplateView):
    """ Vista de pagina de Inicio """
    template_name = "persona/inicio.html"

from applications import departamento
from applications.persona.models import Empleado
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView

from .forms import NewDepartamentoForm
from .models import Departamento


class Pruebaview(TemplateView):
    """ Muestra todos los departamentos

    Args:
        TemplateView ():
    """
    template_name = "departamento/home.html"


class NewDepartamentoView(FormView):
    """ Vista para Crear nuevos Departamentos

    Args:
        Recibe formulario del html

    Returns:
        Form
    """
    template_name = "departamento/new_departamento.html"
    # Se usa form_class para recibir datos
    form_class = NewDepartamentoForm
    success_url = reverse_lazy("persona_app:exito")
    
    def form_valid(self, form):
        """
        departamento = form.cleaned_data["departamento"]
        shortname = form.cleaned_data["shortname"]
        Departamento.objects.create(
            name = departamento
            shot_name = shortname 
        )
        """
        # FORMA ALTERNATIVA DE CREAR ESTO (lo de arriba)
        depa = Departamento(
            name = form.cleaned_data["departamento"],
            shot_name = form.cleaned_data["shortname"],
        )
        depa.save()

        nombre = form.cleaned_data["nombre"]
        apellido = form.cleaned_data["apellido"]
        # Crear segun ORM de django
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = "1",
            departamento = depa,
        )
        return super(NewDepartamentoView,self).form_valid(form)


class DepartamentoListView(ListView):
    """ Muestra todos los departamentos y se puede ver los empleados que hay dentor de cada uno desde el detail

    Args:
        ListView (_type_): _description_
    """
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"

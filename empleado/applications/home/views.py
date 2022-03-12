from django.db.models import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from .forms import PruebaForm
from .models import Prueba



""" *** Aplicacion para pruebas *** """

class PruebaListView(ListView):
    template_name = "home/lista.html"
    # Parametro para envio de datos
    context_object_name = "listaNumeros"
    queryset = ["1", "10", "20", "30", "555"]


class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = "lista"


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    # ver la validacion en el archivo forms.py
    form_class = PruebaForm
    success_url = reverse_lazy("persona_app:exito")


class ResumeFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"

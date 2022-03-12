from django.contrib import admin
from django.urls import path

from . import views

app_name = "departamento_app"

urlpatterns = [
    path(
        'departamento/',
        views.Pruebaview.as_view()
        ),
    path(
        'new_departamento/',
        views.NewDepartamentoView.as_view(),
        name="nuevo_departamento"
        ),
    path(
        'listar_departamentos/',
        views.DepartamentoListView.as_view(),
        name="listar-departamentos"
    ),
]
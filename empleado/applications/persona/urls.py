from django.contrib import admin
from django.urls import path

from applications.persona import views


app_name = "persona_app"

urlpatterns = [
    path(
        'persona/', 
        views.Pruebaview.as_view()
        ),
    path(
        'listar-empleados/', 
        views.ListAllEmpleados.as_view(),
        name="empleados_all"
        ),
    path(
        'empleados-admin/',
        views.ListAllEmpleadosAdmin.as_view(),
        name="empleados_admin"
        ),
    path(
        'editar-empleado/<pk>',
        views.EmpleadoUpdateView.as_view(),
        name="editar_empleado"
    ),
    # Listar segun palabra clave
    path(
        'listar-filtro/<shotname>', 
        views.ListByAreaEmpleado.as_view(),
        name="empleados_area"
        ),
    path(
        'buscar-empleado/', 
        views.ListEmpleadoByKword.as_view()
        ),
    path(
        'habilidades/', 
        views.ListHabilidadesEmpleado.as_view()
        ),
    path(
        'ver-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(),
        name="empleado_detalle"
        ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name="empleado_add"
        ),
    path(
        'success/', 
        views.SuccesView.as_view(), 
        name = "exito",
        ),
    path(
        'delete-empleado/<pk>',
        views.EmpleadoDeleteView.as_view(),
        name="eliminar_empleado",
        ),
    path(
        '',
        views.InicioView.as_view(), name="inicio"
        ),
    
]

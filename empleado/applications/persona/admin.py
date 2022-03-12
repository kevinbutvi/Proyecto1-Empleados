from django.contrib import admin
from .models import Empleado, Habilidades


admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name", 
        "last_name",
        "departamento",
        "job",
        "full_name",
    )

    def full_name(self, obj):
        """ Funcion que devuelve nombre completo de un registro

        Args:
            obj: Nombre y Apellido

        Returns:
            Fullname
        """
        return (obj.first_name + " " + obj.last_name)

    # Filtro de  busqueda tipo campo texto
    search_fields = (
        "first_name",
    )
    # Filtro de lista para seleccionar
    list_filter = (
        "job",
        "habilidades",
    )
    # Filtro Horizontal para buscar dentro de habilidades de empleados
    filter_horizontal = (
        "habilidades",
    )

# Se pasa como parametro el modelo principal y el 2do que es como se va a mostrar, filtros, etc
admin.site.register(Empleado, EmpleadoAdmin)
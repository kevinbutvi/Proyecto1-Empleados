from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include

# IMPORTACIONES necesarias para podes mostrar los archivos MEDIA
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.departamento.urls')),
    path('', include('applications.persona.urls')),
    path('', include('applications.home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

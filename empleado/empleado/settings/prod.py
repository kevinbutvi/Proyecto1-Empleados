from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# SE CAMBIA POR ESTO PARA SOLUCIONAR UN PROBLEMA DE VERSIONES DE DJANGO
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}
"""

STATIC_URL = '/static/'
STATICFILES_DIRS = ["static"] # DECLARACION DE LA UBICACION DE LOS ARCHIVOS ESTATICOS
STATIC_ROOT="staticfiles" #VER SI VA ASI O COMO, NO ESTOY SEGURO SI SE DECLARA ASI

# Lo de abajo es para que los archivos multimedia se guarden por defecto en la carpeta media, y que en la declaracion del "upload to" solo haya que poner la carpeta contenedora
MEDIA_URL = '/media/'
MEDIA_ROOT = "media"

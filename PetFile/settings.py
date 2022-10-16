"""
Django settings for PetFile project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
import os.path
from pathlib import Path

# File path
FILE_DIR = Path(__file__).resolve().parent.parent.parent
MEDIA_URL = '/Files/'
MEDIA_ROOT = os.path.join(FILE_DIR, "Files")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)c&9xx-l2iwt4!)raxb(3l)bfv^0h-2qsof2e81^y-$kvbjkxu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Apps
    # aplicacion para las masotas
    'pet.apps.PetConfig',
    # aplicacion para las aginas que no se ligan a una apliacion espesifica
    'page.apps.PageConfig',
    # aplicaion para el registro login del proyecto
    'user.apps.UserConfig',
    # aplicacion que se encarga del manejo de los procesos de las mascotas
    'process.apps.ProcessConfig',
    # aplicacion para administrar las vacunas de las mascotas
    'vaccine.apps.VaccineConfig',
    # aplicacion que toma los doumentos de los procesos
    'document.apps.DocumentConfig',
    # aplicacion para administrar los tipos de animales
    'pet_type.apps.PetTypeConfig',
    # aplicacion que administra las vistas y procesos que hace un veterinario
    'veterinary.apps.VeterinaryConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PetFile.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # directorio donde se guardarian los templates de las aplicaciones
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins' : [
                'pet.templatetags.filters_group'
            ],
        },
    },
]

WSGI_APPLICATION = 'PetFile.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Apartado de configuracion de la base de datos del proyecto
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',

        'NAME': os.getenv('DBNAME'),
        'USER': os.getenv('DBUSER'),
        'PASSWORD': os.getenv('DBPASS'),
        'HOST': os.getenv('DBHOST'),

        # 'OPTIONS' : {
        #
        #
        #
        #
        #
        #     # # aqui se asigna que se lea el archivo en donde se enuentra lo necesario para hacer la coneccion d ela base de datos
        #     # 'read_default_file' : os.path.join(BASE_DIR, "my.cnf")
        # }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Ruteo de hacia a donde se quiere enviar a las personas que no estan logeadas
LOGIN_URL = 'login'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# apartado de asignacion de directorio de archivos estaticos (CSS)
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





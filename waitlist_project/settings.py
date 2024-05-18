"""
Django settings for waitlist_project project.

Generated by 'django-admin startproject' using Django 5.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
from decouple import config
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default= '21547Mftrcxze587svceO32MpEEEr2')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
     #LOCAL APPS 
    'formulario',
    'listas',
    'usuarios',
    
    #THIRD APPS
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'dj_database_url'
    
    
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True 

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding', 
    'authorization',
    'content-type',
    'dnt',
    'user-agent',
    'x-csrftoken',
    'x-requested-with', 
    'Access-Control-Allow-Headers'#SIEMPRE
]


ROOT_URLCONF = 'waitlist_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',#Especifica que usarás el backend de plantillas de Django.
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Lista de directorios donde Django buscará plantillas.
        'APP_DIRS': True, #Indica a Django que busque plantillas en los directorios templates de cada aplicación instalada.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'waitlist_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASE_URL = config('DATABASE_URL')

DATABASES = {

    'default': dj_database_url.config(                                       
                                      
        default =  dj_database_url.parse(DATABASE_URL), conn_max_age=600)   
        
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'usuarios.User'


REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': [
    
    'rest_framework.authentication.SessionAuthentication',
]
}

EMAIL_SETTINGS_FILE = os.path.join(BASE_DIR, 'email_settings.json')

with open(EMAIL_SETTINGS_FILE) as data_file:
    email_settings = json.load(data_file)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'    
EMAIL_HOST = email_settings['EMAIL_HOST']
EMAIL_HOST_USER = email_settings['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_settings['EMAIL_HOST_PASSWORD']
EMAIL_PORT = email_settings['EMAIL_PORT']
EMAIL_USE_TLS = email_settings['EMAIL_USE_TLS']
DEFAULT_FROM_EMAIL = email_settings['EMAIL_HOST_USER']

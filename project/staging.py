from .base import *
from environs import Env
import os

env = Env()
env.read_env()

DEBUG = False

ALLOWED_HOSTS = ['*']

# Cambios de configuración de archivos estáticos y de medios
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
        'OPTIONS': {
            'bucket_name': AWS_STORAGE_BUCKET_NAME,
            'location': 'media',
        },
    },
    'staticfiles': {
        'BACKEND': 'storages.backends.s3boto3.S3StaticStorage',
        'OPTIONS': {
            'bucket_name': AWS_STORAGE_BUCKET_NAME,
            'location': 'static',
        },
    },
}

# Parámetros de almacenamiento S3 (cache de un día)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  
}

# Base de datos para el entorno de Staging (usa las mismas variables que Development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': '3306',
    }
}

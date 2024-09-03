from .base import *
from environs import Env

env = Env()
env.read_env()

# Configuración específica para Staging
DEBUG = False

ALLOWED_HOSTS = ['*'] 

# Configuración del bucket S3 para Staging
AWS_STORAGE_BUCKET_NAME = env.str('AWS_S3_BUCKET_NAME_STAGING')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# URLs para archivos estáticos y de medios
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# Reconfiguración de STORAGES para usar S3 en Staging
STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
    },
    'staticfiles': {
        'BACKEND': 'storages.backends.s3boto3.S3StaticStorage',
    },
    'mediafiles': {
        'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
        'OPTIONS': {
            'bucket_name': AWS_STORAGE_BUCKET_NAME,
        },
    }
}

# Configuración de la base de datos para Staging
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

# Otros ajustes que podrías necesitar en Staging

# Tiempo de expiración del caché para archivos estáticos en Staging
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

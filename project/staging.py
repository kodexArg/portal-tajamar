from .base import *
from environs import Env
from loguru import logger
import os

env = Env()
env.read_env()

# Activamos el DEBUG temporalmente para obtener más detalles
DEBUG = env.bool('DEBUG', default=False)

# Permitimos cualquier host en este entorno de staging
ALLOWED_HOSTS = ['*']

# Habilitamos logs de que estamos en staging
logger.info("[INFO] Usando configuración de staging.py")

# Configuración de archivos estáticos y de medios
if DEBUG:
    # Modo DEBUG - Utilizando recursos locales
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / 'core/static']

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
    logger.info(f"Using DEBUG MODE:\n - MEDIA_ROOT={MEDIA_ROOT}\n - STATICFILES_DIRS={STATICFILES_DIRS}\n")

else:
    # Configuración de producción en S3
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

# Configuración de la base de datos
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

# Parámetros de almacenamiento S3
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # Cache de un día
}

logger.info("[INFO] Finalizó la carga de staging.py con éxito")

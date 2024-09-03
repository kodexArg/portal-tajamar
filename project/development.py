from .base import *
from environs import Env
import os

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

env = Env()
env.read_env()

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

if DEBUG:
    # Configuración para desarrollo local con archivos estáticos locales
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_DIRS = [BASE_DIR / 'core/static']

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

    STORAGES = {
        'default': {
            'BACKEND': 'django.core.files.storage.FileSystemStorage',
            'OPTIONS': {
                'location': MEDIA_ROOT,
            }
        },
        'staticfiles': {
            'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
            'OPTIONS': {
                'location': STATIC_ROOT,
            }
        },
    }

else:
    # Configuración para desarrollo conectando a S3
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

    # No necesitas STATIC_ROOT ni MEDIA_ROOT porque todo se maneja en S3
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

# Configuración de la base de datos para el entorno de desarrollo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.str('DOCKER_DB_NAME'),
        'USER': env.str('DOCKER_DB_USER'),
        'PASSWORD': env.str('DOCKER_DB_PASSWORD'),
        'HOST': env.str('DOCKER_DB_HOST'),
        'PORT': env.str('DOCKER_DB_PORT', '3306'),
    }
}

# Añadir aplicaciones y middleware específicos para desarrollo
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

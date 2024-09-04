from .base import *
from environs import Env
import os

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

env = Env()
env.read_env()

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

if DEBUG:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / 'core/static']

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
    logger.info(f"Using DEBUG MODE:\n - MEDIA_ROOT={MEDIA_ROOT}\n - STATICFILES_DIRS={STATICFILES_DIRS}\n")

else:
    # S3
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

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

INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

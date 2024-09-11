from .base import *
from environs import Env
from loguru import logger
import os

env = Env()
env.read_env()

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = ['*']

logger.info("[INFO] Usando configuración de staging.py")

if DEBUG:
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / 'core/static']

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
    
    logger.debug(f"Using DEBUG MODE:\n - MEDIA_ROOT={MEDIA_ROOT}\n - STATICFILES_DIRS={STATICFILES_DIRS}")
else:
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
    
    logger.debug(f"STATIC_URL={STATIC_URL}")
    logger.debug(f"STORAGES={STORAGES}")

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

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

logger.info("[INFO] Finalizó la carga de staging.py con éxito")

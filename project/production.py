from .base import *

DEBUG = False
ALLOWED_HOSTS = [f"tajamar-production.{AWS_REGION}.elasticbeanstalk.com"]

AWS_STORAGE_BUCKET_NAME = env.str('AWS_S3_BUCKET_NAME_PRODUCTION')
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/'
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/'

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

import os
from django.core.wsgi import get_wsgi_application

# Use DJANGO_ENV to set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"project.{os.getenv('DJANGO_ENV', 'development')}")

application = get_wsgi_application()

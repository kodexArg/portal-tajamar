import os
from django.core.asgi import get_asgi_application

# Use DJANGO_ENV to set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"project.{os.getenv('DJANGO_ENV', 'development')}")

application = get_asgi_application()

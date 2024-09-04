from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core import views
# Las URLs se configurarían de la siguiente manera en tu urls.py:
# from django.urls import path
# from .views import HomeView, UploadFileView

# urlpatterns = [
#     path('', HomeView.as_view(), name='home'),
#     path('upload/', UploadFileView.as_view(), name='upload_file'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('upload/', views.UploadFileView.as_view(), name='upload_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

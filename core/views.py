from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings
import os

@csrf_exempt
def home(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        file_url = os.path.join(settings.MEDIA_URL, file_name)
        return HttpResponse(f'''
            <div class="notification is-success">
                Archivo subido exitosamente.
            </div>
            <img src="{file_url}" style="max-width: 300px; max-height: 300px; display: block; margin: auto;">
        ''')
    return render(request, 'home.html')

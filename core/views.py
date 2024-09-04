from django.views import View
from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.files.storage import default_storage
from django.conf import settings
from django.template.response import TemplateResponse
from loguru import logger

class HomeView(View):
    def get(self, request, *args, **kwargs):
        logger.info("Renderizando la página de inicio")
        return render(request, 'home.html')

@method_decorator(csrf_exempt, name='dispatch')
class UploadFileView(View):
    def post(self, request, *args, **kwargs):
        logger.info("Método POST recibido")
        
        if request.FILES.get('file'):
            logger.info("Archivo recibido")
            file = request.FILES['file']
            
            try:
                file_name = default_storage.save(file.name, file)
                file_url = f"{settings.MEDIA_URL}{file_name}"
                logger.info(f"Archivo guardado como: {file_name}, accesible en: {file_url}")
                
                context = {'file_url': file_url, 'file_name': file.name}
                return TemplateResponse(request, 'partials/success_box.html', context)
            
            except Exception as e:
                logger.error(f"Error al guardar el archivo: {e}")
                context = {'error_message': 'Error al subir el archivo.'}
                return TemplateResponse(request, 'partials/error_box.html', context)
        else:
            logger.warning("No se encontró ningún archivo en la solicitud POST")
            context = {'error_message': 'No se encontró ningún archivo en la solicitud.'}
            return TemplateResponse(request, 'partials/error_box.html', context)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings
from loguru import logger

def home(request):
    # Solo renderiza la página principal con el formulario
    logger.info("Renderizando la página de inicio")
    return render(request, 'home.html')

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        logger.info("Método POST recibido")
        
        if request.FILES.get('file'):
            logger.info("Archivo recibido")
            file = request.FILES['file']
            
            try:
                file_name = default_storage.save(file.name, file)
                file_url = f"{settings.MEDIA_URL}{file_name}"
                logger.info(f"Archivo guardado como: {file_name}, accesible en: {file_url}")
                
                # Respuesta HTML para actualizar el estado tras la subida exitosa
                return HttpResponse(f'''
                    <div class="notification is-success mt-4">
                        Archivo subido exitosamente: <a href="{file_url}" target="_blank">{file.name}</a>
                    </div>
                ''')
            
            except Exception as e:
                logger.error(f"Error al guardar el archivo: {e}")
                return HttpResponse('''
                    <div class="notification is-danger mt-4">
                        Error al subir el archivo.
                    </div>
                ''')
        else:
            logger.warning("No se encontró ningún archivo en la solicitud POST")
            return HttpResponse('''
                <div class="notification is-danger mt-4">
                    No se encontró ningún archivo en la solicitud.
                </div>
            ''')
    return HttpResponse(status=405)

import os
from django.conf import settings

class StaticFileCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Solo aplicar a archivos estáticos de imágenes
        if request.path.startswith('/static/') and any(request.path.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']):
            # Agregar headers para evitar cache en desarrollo
            if settings.DEBUG:
                response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
                response['Pragma'] = 'no-cache'
                response['Expires'] = '0'
            else:
                # En producción, cache por 1 año
                response['Cache-Control'] = 'public, max-age=31536000'
        
        return response 
from django import template
from django.templatetags.static import static
import os
from django.conf import settings

register = template.Library()

@register.simple_tag
def static_version(path):
    """
    Template tag que agrega un timestamp basado en la fecha de modificación
    del archivo para evitar el cache del navegador
    """
    static_url = static(path)
    
    # Obtener la ruta física del archivo
    static_file_path = os.path.join(settings.STATIC_ROOT, path.lstrip('/'))
    
    try:
        # Obtener la fecha de modificación del archivo
        if os.path.exists(static_file_path):
            timestamp = int(os.path.getmtime(static_file_path))
        else:
            # Si no existe, usar timestamp actual
            import time
            timestamp = int(time.time())
    except:
        # En caso de error, usar timestamp actual
        import time
        timestamp = int(time.time())
    
    return f"{static_url}?v={timestamp}" 
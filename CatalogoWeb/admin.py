from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Producto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria', 'imagen_preview']
    list_filter = ['categoria', 'precio']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio']
    ordering = ['nombre']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'precio')
        }),
        ('Categorización', {
            'fields': ('categoria',)
        }),
        ('Imagen', {
            'fields': ('imagen',)
        }),
    )
    
    def imagen_preview(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" style="height: 50px; width: 50px; object-fit: cover;" />')
        return 'Sin imagen'
    imagen_preview.short_description = 'Imagen'
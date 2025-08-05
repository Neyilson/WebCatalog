from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    
    # Categorías
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    
    # Búsqueda
    path('buscar/', views.buscar_productos, name='buscar_productos'),
    
    # API
    path('api/productos/', views.api_productos, name='api_productos'),
    
    # Panel de administración
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Producto, Categoria

# Vista principal - Página de inicio
def home(request):
    """Vista para la página principal del catálogo"""
    productos_destacados = Producto.objects.all()[:6]  # Últimos 6 productos
    categorias = Categoria.objects.all()
    
    context = {
        'productos_destacados': productos_destacados,
        'categorias': categorias,
    }
    return render(request, 'CatalogoWeb/home.html', context)

# Vista para listar todos los productos
def lista_productos(request):
    """Vista para mostrar todos los productos"""
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    
    # Filtro por categoría
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    # Búsqueda por nombre
    busqueda = request.GET.get('q')
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'categoria_actual': categoria_id,
        'busqueda': busqueda,
    }
    return render(request, 'CatalogoWeb/lista_productos.html', context)

# Vista para mostrar detalles de un producto
def detalle_producto(request, producto_id):
    """Vista para mostrar los detalles de un producto específico"""
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Productos relacionados solo si el producto tiene categoría
    productos_relacionados = []
    if producto.categoria:
        productos_relacionados = Producto.objects.filter(
            categoria=producto.categoria
        ).exclude(id=producto.id)[:4]
    
    categorias = Categoria.objects.all()
    
    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
        'categorias': categorias,
    }
    return render(request, 'CatalogoWeb/detalle_producto.html', context)

# Vista para mostrar productos por categoría
def productos_por_categoria(request, categoria_id):
    """Vista para mostrar productos de una categoría específica"""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    
    context = {
        'categoria': categoria,
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'CatalogoWeb/productos_por_categoria.html', context)

# Vista para búsqueda de productos
def buscar_productos(request):
    """Vista para buscar productos"""
    query = request.GET.get('q', '').strip()
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    
    if query:
        productos = productos.filter(
            nombre__icontains=query
        ) | productos.filter(
            descripcion__icontains=query
        )
    
    context = {
        'productos': productos,
        'query': query,
        'categorias': categorias,
    }
    return render(request, 'CatalogoWeb/buscar_productos.html', context)

# Vista API para obtener productos (opcional, para AJAX)
def api_productos(request):
    """API simple para obtener productos en formato JSON"""
    productos = Producto.objects.all()
    data = []
    
    for producto in productos:
        data.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'categoria': producto.categoria.nombre if producto.categoria else None,
        })
    
    return JsonResponse({'productos': data})

# Vista para el panel de administración personalizado
def admin_panel(request):
    """Vista para un panel de administración básico"""
    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()
    productos_recientes = Producto.objects.all()[:5]
    categorias = Categoria.objects.all()
    
    context = {
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'productos_recientes': productos_recientes,
        'categorias': categorias,
    }
    return render(request, 'CatalogoWeb/admin_panel.html', context)

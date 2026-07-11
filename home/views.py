from django.shortcuts import render
from django.apps import apps
from django.db.models import Q

def index(request):
    return render(request, 'home/index.html')

def buscar(request):
    query = request.GET.get('q', '')
    resultados = []
    
    apps_list = [
        'computadoras', 'electronica', 'hogar', 'moda', 
        'moviles', 'lanzamientos', 'mas_vendidos', 'ofertas'
    ]

    if query:
        for app_name in apps_list:
            try:
                Producto = apps.get_model(app_name, 'Producto')
                productos = Producto.objects.filter(
                    Q(nombre__icontains=query) | Q(descripcion__icontains=query)
                )
                
                for p in productos:
                    p.app_name = app_name
                    resultados.append(p)
            except LookupError:
                continue

    return render(request, 'home/busqueda.html', {'query': query, 'resultados': resultados})

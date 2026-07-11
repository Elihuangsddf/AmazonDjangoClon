from django.shortcuts import render
from .models import Producto

def index(request):
    items = Producto.objects.filter(disponibilidad=True)
    return render(request, 'Lanzamientos/lanzamientos.html', {'items': items, 'titulo': 'Nuevos Lanzamientos'})

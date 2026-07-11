from django.shortcuts import render
from .models import Producto

def index(request):
    items = Producto.objects.filter(disponibilidad=True)
    return render(request, 'Hogar/hogar.html', {'items': items, 'titulo': 'Hogar y Cocina'})

from django.shortcuts import render
from .models import Producto

def index(request):
    items = Producto.objects.filter(disponibilidad=True)
    return render(request, 'Mas_vendidos/mas_vendidos.html', {'items': items, 'titulo': 'Más Vendidos'})

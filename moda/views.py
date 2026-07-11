from django.shortcuts import render
from .models import Producto

def index(request):
    items = Producto.objects.filter(disponibilidad=True)
    return render(request, 'Moda/moda.html', {'items': items, 'titulo': 'Moda'})

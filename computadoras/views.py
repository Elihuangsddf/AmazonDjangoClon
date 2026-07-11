from django.shortcuts import render
from .models import Producto

def index(request):
    items = Producto.objects.filter(disponibilidad=True)
    return render(request, 'Computadoras/computadoras.html', {'items': items, 'titulo': 'Computadoras'})

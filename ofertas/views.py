from django.shortcuts import render
from .models import Oferta

def index(request):
    items = Oferta.objects.all()
    return render(request, 'Ofertas/ofertas.html', {'items': items, 'titulo': 'Ofertas del Día'})

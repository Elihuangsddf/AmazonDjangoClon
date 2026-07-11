from django.shortcuts import render

def index(request):
    return render(request, 'home/products.html', {'items': [], 'titulo': 'Amazon Pay'})

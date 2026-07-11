def totalCarrito(request):
    total = 0
    if 'carrito' in request.session:
        for key, value in request.session['carrito'].items():
            total = total + float(value['precio'])
    return {'totalCarrito': total}
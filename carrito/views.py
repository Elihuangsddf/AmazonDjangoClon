from django.shortcuts import render, redirect
from .carrito import Carrito
from django.apps import apps

def agregarProducto(request, app_name, productoId):
    carrito = Carrito(request)
    Producto = apps.get_model(app_name, 'Producto')
    producto = Producto.objects.get(id=productoId)
    carrito.agregar(producto=producto)
    return redirect("carrito:carritoDetalle")

def eliminarProducto(request, app_name, productoId):
    carrito = Carrito(request)
    Producto = apps.get_model(app_name, 'Producto')
    producto = Producto.objects.get(id=productoId)
    carrito.eliminar(producto=producto)
    return redirect("carrito:carritoDetalle")

def restarProducto(request, app_name, productoId):
    carrito = Carrito(request)
    Producto = apps.get_model(app_name, 'Producto')
    producto = Producto.objects.get(id=productoId)
    carrito.restarProducto(producto=producto)
    return redirect("carrito:carritoDetalle")

def limpiarCarrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito:carritoDetalle")

def carritoDetalle(request):
    return render(request, "carrito/carrito.html")
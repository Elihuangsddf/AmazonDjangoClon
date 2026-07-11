from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.carritoDetalle, name='carritoDetalle'),
    path('agregar/<str:app_name>/<int:productoId>/', views.agregarProducto, name='agregar'),
    path('eliminar/<str:app_name>/<int:productoId>/', views.eliminarProducto, name='eliminar'),
    path('restar/<str:app_name>/<int:productoId>/', views.restarProducto, name='restar'),
    path('limpiar/', views.limpiarCarrito, name='limpiar'),
]

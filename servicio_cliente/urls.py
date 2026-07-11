from django.urls import path
from . import views

app_name = 'servicio_cliente'

urlpatterns = [
    path('', views.index, name='index'),
]

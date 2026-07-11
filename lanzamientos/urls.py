from django.urls import path
from . import views

app_name = 'lanzamientos'

urlpatterns = [
    path('', views.index, name='index'),
]

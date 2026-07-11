from django.urls import path
from . import views

app_name = 'computadoras'

urlpatterns = [
    path('', views.index, name='index'),
]

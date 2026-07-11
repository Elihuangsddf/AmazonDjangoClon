from django.urls import path
from . import views

app_name = 'hogar'

urlpatterns = [
    path('', views.index, name='index'),
]

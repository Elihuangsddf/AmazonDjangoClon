from django.urls import path
from . import views

app_name = 'moda'

urlpatterns = [
    path('', views.index, name='index'),
]

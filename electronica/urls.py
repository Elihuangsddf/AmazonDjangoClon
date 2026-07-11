from django.urls import path
from . import views

app_name = 'electronica'

urlpatterns = [
    path('', views.index, name='index'),
]

from django.urls import path
from . import views

app_name = 'mas_vendidos'

urlpatterns = [
    path('', views.index, name='index'),
]

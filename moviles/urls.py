from django.urls import path
from . import views

app_name = 'moviles'

urlpatterns = [
    path('', views.index, name='index'),
]

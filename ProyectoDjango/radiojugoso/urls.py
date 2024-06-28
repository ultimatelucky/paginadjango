#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/', views.noticias, name='noticias'),
    path('galeria/', views.galeria, name='galeria'),
    path('tienda/', views.tienda, name='tienda'),
    path('contacto/', views.contacto, name='contacto'),
]
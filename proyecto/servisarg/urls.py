from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca',views.acerca, name= "acerca"),
    path('alta_trabajador',views.alta_trabajador, name ="alta_trabajador"),
    path('lista_trabajadores',views.lista_trabajadores, name="lista_trabajadores"),
    
    path('categorias',views.categorias, name="categorias"),
    path('contacto',views.contacto, name="contacto"),
]

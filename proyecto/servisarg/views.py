from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TrabajadorForm, ContactoForm
from .models import Trabajador, Oficio
# Create your views here.

def index(request):
    
    #información ficticia
    customer = {
        'first_name': 'Mauricio',
        'last_name': 'Rodriguez',
        'age': '20',
        'area': 'Flores, CABA',
        'valid': False
        
        
    }
    worker_list = Trabajador.objects.all()
    contex = {
        'simulated_customer':customer,
        'worker_list' : worker_list
        
    }
    return render(request,'servisarg/index.html', contex)

def acerca(request):
    return HttpResponse("<h1><br>Acerca de</h1>")

def alta_trabajador(request):
    if request.method == "POST":
        alta_trabajador_form = TrabajadorForm(request.POST) 
        if alta_trabajador_form.is_valid():
            alta_trabajador_form.save()  #  guarda automáticamente el trabajador
            messages.success(request, 'Usuario dado de alta exitosamente') 
            return redirect("lista_trabajadores")
    else:
        alta_trabajador_form = TrabajadorForm()
    contex = {'form': alta_trabajador_form}
    return render(request, 'servisarg/alta_trabajador.html', contex)

def lista_trabajadores(request):
    context = {}
    
    listado_trabajadores = Trabajador.objects.all().order_by("oficio")
    context["listado_trabajadores"] = listado_trabajadores
    
    return render(request, 'servisarg/lista_trabajadores.html',context)

def categorias(request):
    
    context = {}
    
    lista_categorias = Oficio.objects.all().order_by("nombre")
    
    context["lista_categorias"] = lista_categorias
    
    return render(request, 'servisarg/categorias.html',context)

def contacto(request):
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST) 
        if contacto_form.is_valid():
            contacto_form.save() 
            messages.success(request, 'Consulta enviada exitosamente')
            return redirect("index")
    else:
        contacto_form = ContactoForm()
    contex = {'form': contacto_form}
    return render(request, 'servisarg/contacto.html', contex)

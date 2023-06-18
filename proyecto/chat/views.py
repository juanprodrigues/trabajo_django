from servisarg.models import Trabajador
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse

def room_access_required(view_func):
    def wrapper(request, room_name, *args, **kwargs):
        print("Cargando sala", request.user.username)
        cadena = room_name
        partes = cadena.split("_")
        
        if len(partes) != 2 or not partes[0].isdigit() or not partes[1].isdigit():
            return render(request, "chat/error/error.html")
        
        entero1 = int(partes[0])
        entero2 = int(partes[1])
        
        try:
            user_cliente = User.objects.get(id=entero1)
            user_trabajador = Trabajador.objects.get(id=entero2)
            
            if user_trabajador.username == request.user.username or user_cliente.username == request.user.username:
                if user_trabajador.username == request.user.username:
                    chat_with = user_cliente
                else:
                    chat_with = user_trabajador.usuario
                return view_func(request, room_name, *args, chat_with=chat_with, **kwargs)
            else:
                return render(request, "chat/error/error_permisos.html")
        
        except ObjectDoesNotExist:
            return render(request, "chat/error/error_sala.html")
    
    return wrapper

@room_access_required
def room(request, room_name, chat_with):
    return render(request, "chat/room.html", {"room_name": room_name, "chat_with": chat_with})

from servisarg.models import Trabajador
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static

def room_access_required(view_func):
    def wrapper(request, room_name, *args, **kwargs):
        
        room_name_split = room_name.split("_")
        if len(room_name_split) != 2 or not room_name_split[0].isdigit() or not room_name_split[1].isdigit():
            return render(request, "chat/error/error.html")
        
        if not request.user.photo:
            request.user.photo = 'static/servisarg/img/default_photo.png'
    
        id_cliente = int(room_name_split[0])
        id_trabajador = int(room_name_split[1])
        
        try:
            user_cliente = User.objects.get(id=id_cliente)
            user_trabajador = Trabajador.objects.get(id=id_trabajador)
            
            if user_trabajador.username == request.user.username or user_cliente.username == request.user.username:
                if user_trabajador.username == request.user.username:
                    chat_with = user_cliente
                else:
                    chat_with = user_trabajador.usuario
                    
                if not chat_with.photo:
                    chat_with.photo = 'static/servisarg/img/default_photo.png'

                return view_func(request, room_name, *args, chat_with=chat_with, **kwargs)
            else:
                return render(request, "chat/error/error_permisos.html")
        
        except ObjectDoesNotExist:
            return render(request, "chat/error/error_sala.html")
    
    return wrapper

@room_access_required
def room(request, room_name, chat_with):
    return render(request, "chat/room.html", {"room_name": room_name, "chat_with": chat_with})

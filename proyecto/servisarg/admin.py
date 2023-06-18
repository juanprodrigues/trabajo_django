from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *
from chat.models import *
admin.site.register(Trabajador)
admin.site.register(Oficio)
admin.site.register(Message)
admin.site.register(Conversation)
admin.site.register(ConsultaReclamoSugerencia)

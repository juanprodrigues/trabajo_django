from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Recuerda ejecutar las migraciones después de agregar estos cambios a tus modelos:
## Me funciona en este orden...
# py manage.py makemigrations servisarg
# py manage.py migrate servisarg
# py manage.py makemigrations
# py manage.py migrate


# class Persona(AbstractUser):
#     nombre = models.CharField(max_length=130, verbose_name = "Nombre")
#     apellido = models.CharField(max_length=130, verbose_name = "Apellido")
#     fecha_nacimiento = models.DateField(verbose_name = "Fecha de Nacimiento")
#     dni = models.IntegerField(verbose_name = "DNI",unique=True)
#     direccion = models.CharField(max_length =250 , verbose_name="Dirección")
#     telefono = models.IntegerField( verbose_name = "Telefono",unique=True, validators=[MaxValueValidator(9999999999)])
#     email =models.EmailField(verbose_name = "Email", unique=True)
#     clave = models.CharField(max_length= 20 ,verbose_name = "Contraseña")
    
#     class Meta:
#         abstract = True
    
class Oficio(models.Model):
    nombre = models.CharField(max_length=130, verbose_name="Nombre del Oficio")

    def __str__(self):
        return self.nombre

from django.contrib.auth.models import User, Group, Permission

class Trabajador(AbstractUser):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='trabajador')
    # nombre = models.CharField(max_length=130, verbose_name = "Nombre")
    # username = models.CharField(max_length=130, verbose_name = "UserName")
    # apellido = models.CharField(max_length=130, verbose_name = "Apellido")
    fecha_nacimiento = models.DateField(verbose_name = "Fecha de Nacimiento")
    dni = models.IntegerField(verbose_name = "DNI",unique=True)
    direccion = models.CharField(max_length =250 , verbose_name="Dirección")
    telefono = models.IntegerField( verbose_name = "Telefono",unique=True, validators=[MaxValueValidator(9999999999)])
    # email =models.EmailField(verbose_name = "Email", unique=True)
    # clave = models.CharField(max_length= 20 ,verbose_name = "Contraseña")
    oficio = models.ForeignKey(
        Oficio, on_delete=models.SET_NULL, null=True, related_name='trabajadores'
    )
    descripcion = models.TextField(max_length=700, verbose_name="Descripción")
    tipo_usuario = models.CharField(max_length =250 , verbose_name="Tipo de Usuario")
    foto = models.ImageField(upload_to='trabajador_photos/', blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='trabajador_groups'  # Cambia el nombre del acceso inverso
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='trabajador_user_permissions'  # Cambia el nombre del acceso inverso
    )

class Contacto(models.Model):
    nombre = models.CharField(max_length = 100, verbose_name= "Nombre")
    apellido = models.CharField(max_length = 100, verbose_name="Apellido")    
    email =models.EmailField(verbose_name="Email")
    fecha_consulta = models.DateField(verbose_name = "Fecha de consulta")
    tipo = models.CharField(max_length = 100,verbose_name= "tipo de contacto")
    mensaje = models.CharField(max_length = 100,verbose_name ="Mensaje")
    
    



class Mensaje(models.Model):
    emisor = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.ManyToManyField('ContenidoMensaje', related_name='mensajes')
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.emisor} a {self.receptor}"

class Cliente(models.Model):
    trabajador = models.ForeignKey(
        Trabajador, on_delete=models.CASCADE, related_name='clientes'
    )

    def __str__(self):
        return f"Cliente de {self.trabajador.nombre} {self.trabajador.apellido}"

class ContenidoMensaje(models.Model):
    contenido = models.TextField(verbose_name="Contenido del mensaje")

    def __str__(self):
        return self.contenido

    
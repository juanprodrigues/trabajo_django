from django.contrib.auth.models import User, Group, Permission
from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Recuerda ejecutar las migraciones después de agregar estos cambios a tus modelos:
# Me funciona en este orden...
# py manage.py makemigrations servisarg
# py manage.py migrate servisarg
# py manage.py makemigrations
# py manage.py migrate

# O se puede ejecutar el migration.bat
from django.db.models import ImageField


class Oficio(models.Model):
    nombre = models.CharField(max_length=130, verbose_name="Nombre del Oficio")

    def __str__(self):
        return self.nombre



class Trabajador(AbstractUser):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='trabajador')

    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    dni = models.IntegerField(verbose_name="DNI", unique=True)
    direccion = models.CharField(max_length=250, verbose_name="Dirección")
    telefono = models.IntegerField(verbose_name="Telefono", unique=True, validators=[
                                   MaxValueValidator(9999999999)])
    oficio = models.ForeignKey(
        Oficio, on_delete=models.SET_NULL, null=True, related_name='trabajadores'
    )
    descripcion = models.TextField(max_length=700, verbose_name="Descripción")
    foto = models.ImageField(
        upload_to='trabajador_photos/', blank=True, null=True)
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
        # Cambia el nombre del acceso inverso
        related_name='trabajador_user_permissions'
    )

    class Meta:
        verbose_name_plural = "Trabajadores"
        verbose_name = "Trabajador"


class ConsultaReclamoSugerencia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Email")
    fecha_consulta = models.DateField(verbose_name="Fecha de consulta")
    tipo = models.CharField(max_length=100, verbose_name="tipo de contacto")
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False, verbose_name="Leído")

    class Meta:
        verbose_name_plural = "Consultas, Reclamos y Sugerencias"
        verbose_name = "Consulta, Reclamo o Sugerencia"

User.add_to_class('photo', ImageField(
    upload_to='user_photos', blank=True, null=True))

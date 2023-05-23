# Generated by Django 4.2 on 2023-05-23 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(verbose_name="Nombre")),
                ("apellido", models.CharField(verbose_name="Apellido")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("fecha_consulta", models.DateField(verbose_name="Fecha de consulta")),
                ("tipo", models.CharField(verbose_name="tipo de contacto")),
                ("mensaje", models.CharField(verbose_name="Mensaje")),
            ],
        ),
        migrations.CreateModel(
            name="Oficio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(max_length=130, verbose_name="Nombre del Oficio"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trabajador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=130, verbose_name="Nombre")),
                ("apellido", models.CharField(max_length=130, verbose_name="Apellido")),
                (
                    "fecha_nacimiento",
                    models.DateField(verbose_name="Fecha de Nacimiento"),
                ),
                ("dni", models.IntegerField(unique=True, verbose_name="DNI")),
                (
                    "direccion",
                    models.CharField(max_length=250, verbose_name="Dirección"),
                ),
                ("telefono", models.IntegerField(unique=True, verbose_name="Telefono")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                ("clave", models.CharField(verbose_name="Contraseña")),
                (
                    "descripcion",
                    models.TextField(max_length=700, verbose_name="Descripción"),
                ),
                (
                    "oficio",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="trabajadores",
                        to="servisarg.oficio",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.TextField(
        max_length=255,
        blank=False,
        null=False
    )
    apellido = models.TextField (
        max_length=255,
        blank=False,
        null=False
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Correo electrónico"
    )

    contrasena = models.TextField(
        max_length=255,
        blank=False,
        null=False
    )

    fecha_registro = models.DateTimeField(auto_now_add=True)

class Portafolio(models.Model):
    cantidad_total = models.FloatField(max_length=1000)

class transacciones(models.Model):
    cantidad_ejecutada = models.FloatField(max_length=1000)

    precio_final = models.FloatField(max_length=1000)

    fecha = models.DateTimeField(auto_now_add=True)

class activos(models.Model):
    nom_act = models.TextField(max_length=255)

    simbolo = models.TextField(max_length=255)

    precio_actual = models.FloatField(max_length=1000)

    variacion_diaria = models.FloatField(max_length=1000)

class orden (models.Model):
    tipo_orden = models.TextField(max_length=255)
    cantidad = models.FloatField(max_length=1000)
    precio_unit = models.FloatField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class movimientos (models.Model):
    accion = models.TextField(max_length=255)
    detalle = models.TextField(max_length=255)
    fecha_mv = models.DateTimeField (auto_now_add=True)


from django.db import models
from .choice import estado_dog


# Create your models here.
class huerfano(models.Model):
    Nombre = models.CharField(max_length=200, verbose_name="Nombre")
    Raza = models.CharField(max_length=200, verbose_name="Raza")
    Descripcion = models.TextField(verbose_name="Descripcion")
    Fotografia = models.ImageField(upload_to="core")
    Estado = models.CharField(max_length=200, choices=estado_dog, verbose_name="Estado")
    Created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
    Update = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class meta:
        verbose_name = "huerfano"
        verbose_name_plural = "huerfanos"
        ordering = ["-created"]

    def __str__(self):
        return self.Nombre


class solicitud(models.Model):
    Nombre = models.CharField(max_length=200, verbose_name="Nombre")
    Apellido = models.CharField(max_length=200, verbose_name="Apellido")
    Run = models.CharField(max_length=200, verbose_name="Run")
    FecNac = models.DateField(verbose_name="Fecha de nacimiento")
    Telefono = models.PositiveIntegerField(verbose_name="Telefono")
    Email = models.CharField(max_length=200, verbose_name="Correo Electronio")
    Region = models.CharField(max_length=200, verbose_name="Region")
    Comuna = models.CharField(max_length=200, verbose_name="comuna")
    TipoVivienda = models.CharField(max_length=200, verbose_name="tipo de vivienda")

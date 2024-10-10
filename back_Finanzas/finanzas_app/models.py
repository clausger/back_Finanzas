from django.db import models
from django.contrib.auth.models import User

class Ingreso(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    fuente = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    destino = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fuentes = models.CharField(max_length=255) 
    fecha_ingreso = models.CharField(max_length=4)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (self.nombre)

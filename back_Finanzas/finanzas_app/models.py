from django.db import models

class Ingreso(models.Model):
    id = models.AutoField(primary_key=True)  # Campo 'id' añadido
    description = models.CharField(max_length=255)  # Cambiado de 'descripcion' a 'description'
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Cambiado de 'monto' a 'amount'
    date = models.DateTimeField()  # El usuario ingresa la fecha
    category = models.CharField(max_length=100)
    paymentMethod = models.CharField(max_length=100, null=True, blank=True)  
    note = models.TextField(null=True, blank=True)
    tipo_ingreso = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class Gasto(models.Model):
    id = models.AutoField(primary_key=True)  # Campo 'id' añadido
    description = models.CharField(max_length=255)  # Cambiado de 'descripcion' a 'description'
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Cambiado de 'monto' a 'amount'
    category = models.CharField(max_length=100)
    date = models.DateTimeField()  # El usuario ingresa la fecha
    type = models.CharField(max_length=100, null=True, blank=True)  # Campo 'type' añadido
    paymentMethod = models.CharField(max_length=100, null=True, blank=True)  # Campo 'paymentMethod' añadido
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class IngresoProyectado(models.Model):
    anio = models.IntegerField()
    monto = models.DecimalField(max_digits=20, decimal_places=8)

    def __str__(self):
        return f"Año {self.anio}: {self.monto}"

class Proyecto(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    costo_total = models.DecimalField(max_digits=15, decimal_places=2)
    duracion = models.IntegerField(help_text="Duración en días")
    ingresos_proyectados = models.ManyToManyField(IngresoProyectado, related_name='proyectos')
    roi = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    payback = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total_ingresos = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nombre

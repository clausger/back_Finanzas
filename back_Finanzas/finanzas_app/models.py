from django.db import models

class Ingreso(models.Model):
    id = models.AutoField(primary_key=True)  # Campo 'id' añadido
    description = models.CharField(max_length=255)  # Cambiado de 'descripcion' a 'description'
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Cambiado de 'monto' a 'amount'
    date = models.DateTimeField(auto_now_add=True)  # Cambiado de 'fecha' a 'date'
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
    date = models.DateTimeField(auto_now_add=True)  # Cambiado de 'fecha' a 'date'
    type = models.CharField(max_length=100, null=True, blank=True)  # Campo 'type' añadido
    paymentMethod = models.CharField(max_length=100, null=True, blank=True)  # Campo 'paymentMethod' añadido
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"


class FuenteFinanciacion(models.Model):
    tipo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Opcional
    plazo = models.IntegerField(null=True, blank=True)  # Opcional (en meses o días)

    def __str__(self):
        return f"{self.tipo} - {self.monto}"

class IngresoProyectado(models.Model):
    anio = models.IntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Año {self.anio}: {self.monto}"

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    costo_total = models.DecimalField(max_digits=15,decimal_places=2)
    duracion = models.IntegerField(help_text="Duración en días")
    fecha_inicio = models.DateField()
    fuentes_financiacion = models.ManyToManyField(FuenteFinanciacion, related_name='proyectos')
    ingresos_proyectados = models.ManyToManyField(IngresoProyectado, related_name='proyectos')
    roi = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Nueva columna para ROI


    def __str__(self):
        return self.nombre
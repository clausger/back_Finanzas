from django.db import models

class Ingreso(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=100)
    fuente = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=100, null=True, blank=True)  # paymentMethod
    nota = models.TextField(null=True, blank=True)  # note
    tipo_ingreso = models.CharField(max_length=100, null=True, blank=True)  # incomeType

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    destino = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, null=True, blank=True)  # type
    metodo_pago = models.CharField(max_length=100, null=True, blank=True)  # paymentMethod
    nota = models.TextField(null=True, blank=True)  # note

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"

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
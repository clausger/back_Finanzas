import os
import django

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_Finanzas.settings')

# Inicializar Django
django.setup()

from finanzas_app.models import Ingreso, Gasto, IngresoProyectado, Proyecto

def get_all_records():
    # Obtener todos los registros de Ingreso
    ingresos = Ingreso.objects.all()
    print("\nIngresos:")
    for ingreso in ingresos:
        print(f"ID: {ingreso.id}, Descripción: {ingreso.description}, Monto: {ingreso.amount}, Fecha: {ingreso.date}, Categoría: {ingreso.category}, Método de pago: {ingreso.paymentMethod}, Nota: {ingreso.note}, Tipo de Ingreso: {ingreso.tipo_ingreso}")

    # Obtener todos los registros de Gasto
    gastos = Gasto.objects.all()
    print("\nGastos:")
    for gasto in gastos:
        print(f"ID: {gasto.id}, Descripción: {gasto.description}, Monto: {gasto.amount}, Categoría: {gasto.category}, Fecha: {gasto.date}, Tipo: {gasto.type}, Método de pago: {gasto.paymentMethod}, Nota: {gasto.note}")

    # Obtener todos los registros de IngresoProyectado
    ingresos_proyectados = IngresoProyectado.objects.all()
    print("\nIngresos Proyectados:")
    for ingreso_proyectado in ingresos_proyectados:
        print(f"Año: {ingreso_proyectado.anio}, Monto: {ingreso_proyectado.monto}")

    # Obtener todos los registros de Proyecto
    proyectos = Proyecto.objects.all()
    print("\nProyectos:")
    for proyecto in proyectos:
        print(f"ID: {proyecto.id}, Nombre: {proyecto.nombre}, Descripción: {proyecto.descripcion}, Costo Total: {proyecto.costo_total}, Duración: {proyecto.duracion} días, ROI: {proyecto.roi}")

# Ejecutar la función
get_all_records()
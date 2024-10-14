import os
import django

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_Finanzas.settings')

# Inicializar Django
django.setup()

from finanzas_app.models import Ingreso, Gasto, IngresoProyectado, Proyecto

def delete_all_records():
    Ingreso.objects.all().delete()
    Gasto.objects.all().delete()
    IngresoProyectado.objects.all().delete()
    Proyecto.objects.all().delete()

    print("Todos los registros han sido borrados correctamente.")

delete_all_records()

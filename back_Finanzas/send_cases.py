import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_Finanzas.settings')  # Cambia esto si el nombre de tu proyecto es diferente
django.setup()

# Ahora puedes importar los modelos y funciones
from finanzas_app import models
from finanzas_app.models import Ingreso, Gasto
from back_Finanzas.core_connector.connector import enviar_mensaje
from sender import Modules, Types
from django.db.models import Sum

# Clase para representar los mensajes
class Mensaje:
    def __init__(self, usecase, payload, target):
        self.usecase = usecase
        self.payload = payload
        self.target = target

    def to_dict(self):
        return {
            "usecase": self.usecase,
            "payload": self.payload,
            "target": self.target
        }

# Funciones de obtención de datos (las mismas que definiste antes)
def obtener_todas_inversiones():
    return list(Ingreso.objects.filter(category="Inversión").values())

def obtener_inversiones_usuario(username):
    return list(Ingreso.objects.filter(category="Inversión", note=username).values())

def obtener_balance_general():
    total_ingresos = Ingreso.objects.aggregate(total=Sum("amount"))["total"] or 0
    total_gastos = Gasto.objects.aggregate(total=Sum("amount"))["total"] or 0
    balance = total_ingresos - total_gastos
    return {"total_ingresos": total_ingresos, "total_gastos": total_gastos, "balance": balance}

# Obtener datos
todas_inversiones = obtener_todas_inversiones()
inversiones_usuario = obtener_inversiones_usuario("juan.perez")
balance_general = obtener_balance_general()

# Define los casos de uso
casos = [
    Mensaje(usecase="Inversiones", payload=todas_inversiones, target=None),
    Mensaje(usecase="Inversiones", payload=inversiones_usuario, target="juan.perez"),
    Mensaje(usecase="Balance", payload=balance_general, target=None),
]

# Enviar cada caso de uso
for caso in casos:
    try:
        enviar_mensaje(
            origen=Modules.GESTION_FINANCIERA.value,
            destino=Modules.USUARIO.value,
            mensaje=caso,
            caso_uso=caso.usecase,
            tipo_dato=Types.JSON.value,
            target=caso.target or "",
            status="200",
            user="default_user"
        )
        print(f"Mensaje enviado para el caso de uso: {caso.usecase}")
    except Exception as e:
        print(f"Error al enviar el mensaje para {caso.usecase}: {e}")

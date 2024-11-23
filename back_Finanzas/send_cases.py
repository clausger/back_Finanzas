import os
import django
import requests

from sender import *

# Configura el entorno de Django
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_Finanzas.settings')  # Cambia esto si el nombre de tu proyecto es diferente
#django.setup()

# Ahora puedes importar los modelos y funciones
#from finanzas_app.models import Ingreso, Gasto
from back_Finanzas.core_connector.connector import enviar_mensaje
import sender
#from django.db.models import Sum

# Funciones de obtención de datos
def obtener_todas_inversiones():

    api_url = "https://back-finanzas.onrender.com/api/ingresos/"

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()

        inversiones = [
            float(ingreso["amount"]) for ingreso in data if ingreso.get("category") == "Inversiones"
        ]

        return inversiones

    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return []


def obtener_inversiones_usuario(username):
    #return list(Ingreso.objects.filter(category="Inversión", note=username).values())
    return {'numero':'0'}

def obtener_balance_general():

    api_url = "https://back-finanzas.onrender.com/api/resumen/"

    try:

        response = requests.get(api_url)
        response.raise_for_status()  # Lanza una excepción si ocurre un error


        data = response.json()


        total_ingresos = data.get("total_ingresos_recurrentes", 0)
        total_gastos = data.get("total_gastos_recurrentes", 0)
        balance_general = data.get("total_balance", 0)


        return {
            "total_ingresos": total_ingresos,
            "total_gastos": total_gastos,
            "balance_general": balance_general
        }
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el balance general desde la API: {e}")
        return {
            "total_ingresos": 0,
            "total_gastos": 0,
            "balance_general": 0
        }

# Obtener datos
todas_inversiones = obtener_todas_inversiones()
inversiones_usuario = obtener_inversiones_usuario("juan.perez")
balance_general = obtener_balance_general()

# Define los casos de uso
casos = [
    {"usecase": "Inversiones", "payload": todas_inversiones, "target": None},
    {"usecase": "Inversiones", "payload": inversiones_usuario, "target": "juan.perez"},
    {"usecase": "Balance", "payload": balance_general, "target": None},
]

# Enviar cada caso de uso
for caso in casos:
    try:
        enviar_mensaje(
            Modules.GESTION_FINANCIERA.value,  # Origen
            Modules.USUARIO.value,  # Destino
            caso["payload"],                             # Mensaje
            caso["usecase"],                  # Caso de uso
            Types.ARRAY.value                 # Tipo de dato
        )
        print(f"Mensaje enviado para el caso de uso: {caso['usecase']}")
    except Exception as e:
        print(f"Error al enviar el mensaje para {caso['usecase']}: {e}")
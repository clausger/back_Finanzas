from datetime import datetime

import requests
import sender
from sender import start_connection, start_consumer, publish, close_connection, convert_class, convert_body, convert_payload, Types, Modules
from .config import HOST, PORT, USER, PASSWORD, TOKEN
import sqlite3


# Inicializa las conexiones de consumo y publicación
pool_connections = [
    start_connection(HOST, PORT, USER, PASSWORD),
    start_connection(HOST, PORT, USER, PASSWORD)
]

# Función callback para procesar mensajes recibidos
def new_callback(ch, method, properties, body):
    try:
        # Convierte el cuerpo del mensaje a JSON
        message = convert_body(body)

        # Extrae el caso de uso y otros datos
        usecase = message.get("case")
        payload = message.get("payload")
        target = message.get("target")

        # Maneja los diferentes casos de uso
        if usecase == "Balance":
            balance_general = obtener_balance_general()
            print(f"[Balance] Enviando balance: {payload}")
            try:
                enviar_mensaje(
                    Modules.GESTION_FINANCIERA.value,  # Origen
                    Modules.GESTION_FINANCIERA.value,  # Destino
                    balance_general,  # Mensaje
                    usecase,  # Caso de uso
                    Types.ARRAY.value  # Tipo de dato
                )
                print(f"[Balance] Enviando balance calculado: {balance_general}")
            except Exception as e:
                print(f"Error al enviar el mensaje para {usecase}: {e}")

        elif usecase == "Inversion":
            print(f"[Inversion] Guardando inversión: {payload} para usuario: {payload.get('username')}")
            try:
                api_url="https://back-finanzas.onrender.com/api/ingresos/"

                nuevo_ingreso = {
                    "description": "Inversion",
                    "amount": payload.get('monto'),  # Monto del payload
                    "date": payload.get("date", datetime.now().isoformat()),  # Fecha actual si no está en el payload
                    "category": "Inversiones",
                    "paymentMethod": None,
                    "note": None,
                    "tipo_ingreso": "Único",
                    "usuario": payload.get('username'),  # Usuario objetivo del mensaje
                }

                print(nuevo_ingreso)

                response = requests.post(api_url, json=nuevo_ingreso)
                response.raise_for_status()

                print(f"[Inversion] Ingreso guardado exitosamente: {response.json()}")

            except requests.exceptions.RequestException as e:
                print(f"Error al guardar la inversión: {e}")


        elif usecase == "Inversiones":
            if payload:  # Si se solicita inversiones de un usuario específico
                inversiones = obtener_inversiones_usuario(username=payload.get("username"))
                print(f"[Balance] Enviando inversiones del usuario: {payload}")
                try:
                    enviar_mensaje(
                        Modules.GESTION_FINANCIERA.value,  # Origen
                        Modules.GESTION_FINANCIERA.value,  # Destino
                        inversiones,  # Mensaje
                        usecase,  # Caso de uso
                        Types.ARRAY.value  # Tipo de dato
                    )

                except Exception as e:
                    print(f"Error al enviar el mensaje para {usecase}: {e}")


                else:  # Si se solicitan todas las inversiones
                    inversiones = obtener_todas_inversiones()
                    print(f"[Balance] Enviando todas las inversiones:")
                    try:
                        enviar_mensaje(
                            Modules.GESTION_FINANCIERA.value,  # Origen
                            Modules.GESTION_FINANCIERA.value,  # Destino
                            inversiones,  # Mensaje
                            usecase,  # Caso de uso
                            Types.ARRAY.value  # Tipo de dato
                        )

                    except Exception as e:
                        print(f"Error al enviar el mensaje para {usecase}: {e}")


        elif usecase == "balance":
            print(f"[Balance E-Commerce] Mensaje recibido con payload: {payload} y target: {target}")
            try:
                api_ingresos = "https://back-finanzas.onrender.com/api/ingresos/"
                api_gastos = "https://back-finanzas.onrender.com/api/gastos/"

                nuevo_ingreso = {
                    "description": "Ventas E-Commerce",
                    "amount": payload.get('montoVentas'),  # Monto del payload
                    "date": payload.get("date", datetime.now().isoformat()),  # Fecha actual si no está en el payload
                    "category": "Ventas",
                    "paymentMethod": None,
                    "note": None,
                    "tipo_ingreso": "Recurrente",
                    "usuario": None
                }

                print(nuevo_ingreso)

                nuevo_gasto = {
                    "description": "Compras E-Commerce",
                    "amount": payload.get('montoCompras'),  # Monto del payload
                    "date": payload.get("date", datetime.now().isoformat()),  # Fecha actual si no está en el payload
                    "category": "Compras",
                    "paymentMethod": None,
                    "note": None,
                    "tipo_ingreso": "Recurrente",
                    "usuario": None
                }
                print(nuevo_gasto)

                response_ingresos = requests.post(api_ingresos, json=nuevo_ingreso)
                response_ingresos.raise_for_status()

                response_gastos = requests.post(api_gastos, json=nuevo_gasto)
                response_gastos.raise_for_status()


                print(f"[Inversion] Ingreso guardado exitosamente: {response_ingresos.json()}")
                print(f"[Inversion] Ingreso guardado exitosamente: {response_gastos.json()}")

            except requests.exceptions.RequestException as e:
                print(f"Error al guardar la inversión o gasto: {e}")

        else:
            print(f"[Error] Caso de uso no reconocido: {usecase}")

    except Exception as e:
        print(f"Error al procesar el mensaje: {e}")
        print(f"Mensaje original: {body}")

# Configura el callback en sender
sender.callback = new_callback

# Función para iniciar el consumidor
def iniciar_consumidor():
    try:
        start_consumer(pool_connections[0], Modules.GESTION_FINANCIERA.value)
    except Exception as e:
        print(f"Error al iniciar el consumidor: {e}")

# Función para enviar mensajes
def enviar_mensaje(origen, destino, mensaje, caso_uso, tipo_dato="JSON", target="", status="600", user="gestion_financiera"):
    try:
        #mensaje_json = convert_class(mensaje)
        mensaje_json = mensaje
        publish(pool_connections[1], mensaje_json, origen, destino, caso_uso, TOKEN, tipo_dato, target, status, user)
        print(f"Mensaje enviado: {mensaje_json}")

    except Exception as e:
        print(f"Error al enviar mensaje: {e}")
        print(f"Mensaje original: {mensaje}")

# Funciones para cerrar conexiones
def cerrar_publicacion():
    try:
        close_connection(pool_connections[1])
        print("Conexión de publicación cerrada correctamente.")
    except Exception as e:
        print(f"Error al cerrar la conexión de publicación: {e}")

def cerrar_consumidor():
    try:
        close_connection(pool_connections[0])
        print("Conexión del consumidor cerrada correctamente.")
    except Exception as e:
        print(f"Error al cerrar la conexión del consumidor: {e}")

# Conexión a la base de datos SQLite3
def conectar_db():
    return sqlite3.connect("db.sqlite3")

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

    api_url = "https://back-finanzas.onrender.com/api/ingresos/"

    try:
        # Realizar la solicitud GET a la API
        response = requests.get(api_url)
        response.raise_for_status()  # Asegurarse de que no hubo errores en la solicitud

        # Convertir la respuesta a formato JSON
        data = response.json()

        # Filtrar solo los ingresos que son inversiones y pertenecen al usuario
        inversiones = [
            float(ingreso["amount"])
            for ingreso in data
            if ingreso.get("category") == "Inversiones" and ingreso.get("usuario") == username
        ]

        # Retornar las inversiones del usuario
        return inversiones

    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión o solicitud
        print(f"Error al conectar con la API: {e}")
        return []
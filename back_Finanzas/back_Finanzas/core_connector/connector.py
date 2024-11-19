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
        usecase = message.get("usecase")
        payload = message.get("payload")
        target = message.get("target")

        # Maneja los diferentes casos de uso
        if usecase == "Balance":
            print(f"[Balance] Enviando balance: {payload}")
            # Aquí podrías ejecutar lógica para enviar el balance

        elif usecase == "Inversion":
            print(f"[Inversion] Guardando inversión: {payload} para usuario: {target}")
            # Aquí podrías guardar la inversión en tu base de datos

        elif usecase == "Inversiones":
            if payload:  # Si se solicita inversiones de un usuario específico
                print(f"[Inversiones] Enviando inversiones de {payload}")
            else:  # Si se solicitan todas las inversiones
                print("[Inversiones] Enviando todas las inversiones")

        elif usecase == "Prueba":
            print(f"[Prueba] Mensaje recibido con payload: {payload} y target: {target}")


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
def enviar_mensaje(origen, destino, mensaje, caso_uso, tipo_dato="JSON", target="", status="600", user="default_user"):
    try:
        mensaje_json = convert_class(mensaje)
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
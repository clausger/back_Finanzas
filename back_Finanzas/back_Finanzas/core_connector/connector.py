import sender
from sender import start_connection, start_consumer, publish, close_connection, convert_class, convert_body, convert_payload, Types, Modules 
from .config import HOST, PORT, USER, PASSWORD, TOKEN

# Inicializa las conexiones de consumo y publicación
pool_connections = [
    start_connection(HOST, PORT, USER, PASSWORD),
    start_connection(HOST, PORT, USER, PASSWORD)
]

# Función callback para procesar mensajes recibidos
def new_callback(ch, method, properties, body):
    message = convert_body(body)
    payload = message.get('payload')
    try:
        usuario = convert_payload(payload)
        print("Mensaje recibido:", usuario)
    except Exception as e:
        print("Error al procesar el mensaje:", e)
 
# Configura el callback en sender
sender.callback = new_callback

# Función para iniciar el consumidor
def iniciar_consumidor():
    start_consumer(pool_connections[0], Modules.GESTION_FINANCIERA.value)

# Función para enviar mensajes
def enviar_mensaje(origen, destino, mensaje, caso_uso, tipo_dato="JSON"):
    mensaje_json = convert_class(mensaje)
    # Añade los argumentos adicionales: target, status y user
    target = ""  
    status = "600"       
    user = "default_user"   

    publish(pool_connections[1], mensaje_json, origen, destino, caso_uso, TOKEN, tipo_dato, target, status, user)


# Función para cerrar conexiones
def cerrar_publicacion():
    close_connection(pool_connections[1])

def cerrar_consumidor():
    close_connection(pool_connections[0])

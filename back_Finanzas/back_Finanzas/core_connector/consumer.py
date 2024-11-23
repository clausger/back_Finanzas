import sender
from sender import convert_body
import json

def procesar_mensaje(ch, method, properties, body):
    try:
        mensaje = convert_body(body)  # Convierte de bytes a JSON
        usecase = mensaje.get("usecase")
        payload = mensaje.get("payload")
        target = mensaje.get("target")

        # Procesar según el caso de uso
        if usecase == "Balance":
            # Enviar el objeto Balance (simulado aquí como un print)
            print(f"Enviando balance: {payload}")

        elif usecase == "Inversion":
            # Guardar la inversión recibida en la BDD
            print(f"Guardando inversión: {payload} para usuario: {target}")

        elif usecase == "Inversiones":
            if payload:  # Si se solicita inversiones de un usuario específico
                print(f"Enviando inversiones de {payload}")
            else:  # Si se solicitan todas las inversiones
                print("Enviando todas las inversiones")

        elif usecase == "Prueba":
            # Caso de Prueba
            print(f"[Prueba] Mensaje recibido con payload:{payload} y target: {target}")
                
        else:
            print(f"Caso de uso no reconocido: {usecase}")

    except Exception as e:
        print(f"Error al procesar el mensaje: {e}")

# Configura el callback en sender
sender.callback = procesar_mensaje

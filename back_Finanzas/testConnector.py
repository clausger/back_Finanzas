from back_Finanzas.core_connector.connector import iniciar_consumidor, enviar_mensaje, cerrar_conexiones
from sender import Modules, Types

# Define la clase Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def to_dict(self):
        return {
            "nombre": self.nombre
        }

# Inicia el consumidor
iniciar_consumidor()

# Crea un usuario de prueba en lugar de un diccionario
mensaje_prueba = Usuario(nombre="Matias")

# Envía el mensaje usando Types.JSON.value o "JSON" si .value no está disponible
enviar_mensaje(Modules.GESTION_FINANCIERA.value, Modules.GESTION_FINANCIERA.value, mensaje_prueba, 'Prueba', Types.JSON.value)

# Cierra las conexiones
cerrar_conexiones()
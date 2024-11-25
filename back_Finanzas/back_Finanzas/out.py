import sender
from sender import *
from core_connector.config import *
import json

pool_connections = []
pool_channels = []

for i in range(1):
    pool_connections.append(
        start_connection(
            HOST,
            PORT,
            USER,
            PASSWORD
        )
    )
    pool_channels.append(
        pool_connections[i].channel()
    )

auth = sender.Authenticator(pool_connections[0], pool_channels[0], Modules.USUARIO.value)

si = {
  'user': USER,
  'password': PASSWORD,
  'case': 'login',
  'origin': USER
}

result = json.dumps(si)

resultado = auth.authenticate(result) # Si es aceptado recibirá un token como respuesta y sino un String vacío
print("Resultado:",resultado)
close_connection(pool_connections[0])
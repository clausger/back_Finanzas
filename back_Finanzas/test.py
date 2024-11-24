from sys import modules

from back_Finanzas.core_connector.connector import enviar_mensaje
from sender import *

inversion ={
    "monto": "1000",
    "username": "lebron",
}



try:
    enviar_mensaje(Modules.GESTION_FINANCIERA.value,
                   Modules.GESTION_FINANCIERA.value,
                   inversion,
                   "Inversion",
                   Types.JSON.value,
                   "",
                   "600",
                   "gestion_financiera",
                   )
except Exception as e:
    print(f'Error al enviar el mensaje para {"Inversion"}')

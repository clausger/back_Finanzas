from sys import modules

from back_Finanzas.core_connector.connector import enviar_mensaje
from sender import *


inversion =\
    {
    "monto": 999,
    "username": "MP999999"
}




try:
    enviar_mensaje(Modules.GESTION_FINANCIERA.value,
                   Modules.USUARIO.value,
                   inversion,
                   "Inversiones",
                   Types.JSON.value,
                   "MP999999",
                   "600",
                   "{user: gestion_financiera, password: M$!2$4$2#&$m!52*3747}",
                   )
except Exception as e:
    print(f'Error al enviar el mensaje para {"Inversion"}')

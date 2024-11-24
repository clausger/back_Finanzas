import os

# Configuración de conexión
HOST = os.getenv('CORE_HOST', '3.141.117.124')
PORT = int(os.getenv('CORE_PORT', 5672))
USER = os.getenv('CORE_USER', 'gestion_financiera')
PASSWORD = os.getenv('CORE_PASSWORD', 'M$!2$4$2#&$m!52*3747')
TOKEN = os.getenv('CORE_TOKEN', '')
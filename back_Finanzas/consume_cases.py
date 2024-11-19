from back_Finanzas.core_connector.connector import iniciar_consumidor
try:
    print("Iniciando consumidor para casos de uso...")
    iniciar_consumidor()
except Exception as e:
    print(f"Error al iniciar el consumidor: {e}")

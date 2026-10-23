from infraestructura.repositorios import SQLiteRepository, PostgresRepository, OracleRepository
from aplicacion.casos_de_uso import CrearFacturaUseCase
from adaptadores.controladores import WebController, RabbitMQListener

def main():
    print("="*60)
    print(" INICIANDO SISTEMA CON ARQUITECTURA LIMPIA ")
    print("="*60)
    
    # 1. Resolución de dependencias (Infraestructura)
    # Por requerimiento, el cambio de DB es solo configuración. Aquí se usa SQLite funcional.
    repositorio_activo = SQLiteRepository() 
    
    # 2. Instanciación de Capa de Aplicación
    caso_uso = CrearFacturaUseCase(repositorio=repositorio_activo)
    
    # 3. Instanciación de Adaptadores de Entrada
    api_web = WebController(caso_uso=caso_uso)
    broker_rabbitmq = RabbitMQListener(caso_uso=caso_uso)
    
    # --- PRUEBAS FUNCIONALES ---
    
    print("\n--- PRUEBA 1: API WEB (Flujo Exitoso) ---")
    api_web.procesar_peticion_http({"cliente": "Cliente Web Corp", "monto": 1500.50})
    
    print("\n--- PRUEBA 2: BROKER MENSAJERÍA (Flujo Exitoso) ---")
    broker_rabbitmq.consumir_mensaje({"cliente": "Cliente Async Inc", "monto": 350.00})
    
    print("\n--- PRUEBA 3: REGLA DE FRAUDE DESDE API (Monto excesivo) ---")
    api_web.procesar_peticion_http({"cliente": "Estafador S.A.", "monto": 50000.00})
    
    print("\n--- PRUEBA 4: REGLA DE FRAUDE DESDE BROKER (Monto excesivo) ---")
    broker_rabbitmq.consumir_mensaje({"cliente": "Hacker LLC", "monto": 99999.00})
    
    print("\n" + "="*60)

if __name__ == '__main__':
    main()

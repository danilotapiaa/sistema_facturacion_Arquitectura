from aplicacion.puertos_entrada import CrearFacturaInputPort

class WebController:
    def __init__(self, caso_uso: CrearFacturaInputPort):
        self.caso_uso = caso_uso

    def procesar_peticion_http(self, request_body: dict):
        print("[API Web] -> POST /facturas recibiendo datos...")
        try:
            resultado = self.caso_uso.ejecutar(request_body)
            print(f"[API Web] -> HTTP 201 Created: {resultado}")
        except Exception as e:
            print(f"[API Web] -> HTTP 400 Bad Request: {str(e)}")

class RabbitMQListener:
    def __init__(self, caso_uso: CrearFacturaInputPort):
        self.caso_uso = caso_uso

    def consumir_mensaje(self, mensaje_amqp: dict):
        print("[RabbitMQ] -> Consumiendo evento 'crear.factura' de la cola...")
        try:
            resultado = self.caso_uso.ejecutar(mensaje_amqp)
            print(f"[RabbitMQ] -> Evento procesado (ACK): {resultado}")
        except Exception as e:
            print(f"[RabbitMQ] -> Error procesando evento (NACK): {str(e)}")

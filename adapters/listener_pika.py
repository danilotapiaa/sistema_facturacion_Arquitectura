from adapters.input_port import FacturaInputPort

class RabbitMQListener:
    """Adaptador: Consumidor AMQP: RabbitMQ"""
    def __init__(self, input_port: FacturaInputPort):
        self.input_port = input_port

    def consumir_mensaje(self, payload: dict):
        pass

from abc import ABC, abstractmethod

class CrearFacturaInputPort(ABC):
    @abstractmethod
    def ejecutar(self, datos_factura: dict) -> dict:
        pass

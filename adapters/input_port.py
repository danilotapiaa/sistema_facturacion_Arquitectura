from abc import ABC, abstractmethod
from domain.entidad_factura import Factura

class FacturaInputPort(ABC):
    """Puerto de Entrada: Interfaz Crear Factura (Pertenece a Adaptadores según diagrama)"""
    @abstractmethod
    def crear_factura(self, cliente: str, monto: float) -> Factura:
        pass

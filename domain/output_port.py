from abc import ABC, abstractmethod
from .entidad_factura import Factura

class FacturaRepositoryPort(ABC):
    """Puerto de Salida: Interfaz Repositorio (Pertenece al Dominio según diagrama)"""
    @abstractmethod
    def guardar(self, factura: Factura) -> Factura:
        pass

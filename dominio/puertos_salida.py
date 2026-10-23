from abc import ABC, abstractmethod
from .entidades import Factura

class FacturaRepositoryPort(ABC):
    @abstractmethod
    def guardar(self, factura: Factura) -> None:
        pass

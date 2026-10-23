from domain.entidad_factura import Factura
from domain.output_port import FacturaRepositoryPort

class OracleRepository(FacturaRepositoryPort):
    """Adaptador DB: Oracle"""
    def guardar(self, factura: Factura) -> Factura:
        pass

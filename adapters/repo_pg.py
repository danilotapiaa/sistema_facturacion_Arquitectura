from domain.entidad_factura import Factura
from domain.output_port import FacturaRepositoryPort

class PostgreSQLRepository(FacturaRepositoryPort):
    """Adaptador DB: PostgreSQL"""
    def guardar(self, factura: Factura) -> Factura:
        pass

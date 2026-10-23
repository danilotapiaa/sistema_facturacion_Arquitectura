from domain.entidad_factura import Factura
from domain.reglas_negocio import control_de_fraude, politicas_fiscales
from domain.output_port import FacturaRepositoryPort
from adapters.input_port import FacturaInputPort

class CrearFacturaUseCase(FacturaInputPort):
    """Caso de Uso: CrearFacturaUseCase"""
    def __init__(self, repository: FacturaRepositoryPort):
        self.repository = repository

    def crear_factura(self, cliente: str, monto: float) -> Factura:
        factura = Factura(cliente=cliente, monto=monto)
        
        # Validaciones del dominio
        control_de_fraude(factura)
        factura = politicas_fiscales(factura)
        factura.estado = "APROBADA"
        
        # Guardar mediante el puerto de salida
        return self.repository.guardar(factura)

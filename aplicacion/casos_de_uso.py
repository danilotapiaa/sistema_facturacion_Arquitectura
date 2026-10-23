from .puertos_entrada import CrearFacturaInputPort
from dominio.entidades import Factura
from dominio.reglas import ControlFraude, PoliticasFiscales
from dominio.puertos_salida import FacturaRepositoryPort
import uuid

class CrearFacturaUseCase(CrearFacturaInputPort):
    def __init__(self, repositorio: FacturaRepositoryPort):
        self.repositorio = repositorio

    def ejecutar(self, datos_factura: dict) -> dict:
        monto = datos_factura.get("monto", 0.0)
        cliente = datos_factura.get("cliente", "Desconocido")
        
        # 1. Validar reglas de negocio (Fraude)
        ControlFraude.validar(monto)
        
        # 2. Crear Entidad
        factura = Factura(id=str(uuid.uuid4())[:8], monto=monto, cliente=cliente)
        
        # 3. Aplicar reglas de negocio (Fiscales)
        PoliticasFiscales.aplicar(factura)
        
        # 4. Persistir a través del puerto de salida (Polimorfismo)
        self.repositorio.guardar(factura)
        
        return {"status": "success", "factura_id": factura.id, "aprobada": factura.aprobada_fiscalmente}

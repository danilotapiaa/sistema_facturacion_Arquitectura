from dataclasses import dataclass

@dataclass
class Factura:
    id: str
    monto: float
    cliente: str
    aprobada_fiscalmente: bool = False

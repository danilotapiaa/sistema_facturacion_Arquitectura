from dataclasses import dataclass
from typing import Optional

@dataclass
class Factura:
    cliente: str
    monto: float
    id: Optional[int] = None
    estado: str = "PENDIENTE"

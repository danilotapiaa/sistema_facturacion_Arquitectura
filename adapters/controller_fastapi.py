from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from adapters.input_port import FacturaInputPort

router = APIRouter()

class FacturaRequest(BaseModel):
    cliente: str
    monto: float

# El caso de uso se inyectará desde la infraestructura
use_case_instance: FacturaInputPort = None 

def set_use_case(uc: FacturaInputPort):
    global use_case_instance
    use_case_instance = uc

@router.post("/facturas/")
def api_crear_factura(request: FacturaRequest):
    """API REST: FastAPI (Controlador)"""
    try:
        factura_creada = use_case_instance.crear_factura(cliente=request.cliente, monto=request.monto)
        return {"mensaje": "Factura procesada con éxito", "factura": factura_creada}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

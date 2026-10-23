from .entidad_factura import Factura

def control_de_fraude(factura: Factura) -> bool:
    if factura.monto > 10000:
        raise ValueError("Alerta de Fraude: El monto excede el límite permitido.")
    return True

def politicas_fiscales(factura: Factura) -> Factura:
    impuesto = factura.monto * 0.15  # 15% IVA
    factura.monto += impuesto
    return factura

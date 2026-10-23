from .entidades import Factura

class ControlFraude:
    @staticmethod
    def validar(monto: float) -> bool:
        if monto > 10000:
            raise ValueError("Alerta de Fraude: El monto excede el límite permitido de $10,000.")
        return True

class PoliticasFiscales:
    @staticmethod
    def aplicar(factura: Factura):
        if factura.monto > 0:
            factura.aprobada_fiscalmente = True

import sqlite3
from domain.entidad_factura import Factura
from domain.output_port import FacturaRepositoryPort

class SQLiteRepository(FacturaRepositoryPort):
    """Adaptador DB: SQLite"""
    def __init__(self, db_connection):
        self.conn = db_connection
        self._crear_tabla()

    def _crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS facturas 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, cliente TEXT, monto REAL, estado TEXT)''')
        self.conn.commit()

    def guardar(self, factura: Factura) -> Factura:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO facturas (cliente, monto, estado) VALUES (?, ?, ?)",
                       (factura.cliente, factura.monto, factura.estado))
        self.conn.commit()
        factura.id = cursor.lastrowid
        return factura

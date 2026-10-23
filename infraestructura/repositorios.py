from dominio.puertos_salida import FacturaRepositoryPort
from dominio.entidades import Factura
import sqlite3

class PostgresRepository(FacturaRepositoryPort):
    def guardar(self, factura: Factura) -> None:
        # Interfaz de base de datos PostgreSQL con pass
        pass

class OracleRepository(FacturaRepositoryPort):
    def guardar(self, factura: Factura) -> None:
        # Interfaz de base de datos Oracle con pass
        pass

class SQLiteRepository(FacturaRepositoryPort):
    def __init__(self):
        # Base de datos funcional en memoria para pruebas
        self.conn = sqlite3.connect(':memory:', check_same_thread=False)
        self._crear_tabla()

    def _crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS facturas (
                id TEXT PRIMARY KEY,
                monto REAL,
                cliente TEXT,
                aprobada_fiscalmente BOOLEAN
            )
        ''')
        self.conn.commit()

    def guardar(self, factura: Factura) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO facturas (id, monto, cliente, aprobada_fiscalmente) VALUES (?, ?, ?, ?)",
            (factura.id, factura.monto, factura.cliente, factura.aprobada_fiscalmente)
        )
        self.conn.commit()
        print(f"[Infraestructura] -> (SQLite) Factura {factura.id} guardada en memoria.")

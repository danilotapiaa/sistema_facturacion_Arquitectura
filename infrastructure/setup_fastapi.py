import asyncio
from fastapi import FastAPI
from infrastructure.db_sqlite import get_sqlite_connection
from adapters.repo_sqlite import SQLiteRepository
from application.uc_factura import CrearFacturaUseCase
from adapters.controller_fastapi import router, set_use_case
from infrastructure.cliente_web import ejecutar_autoprueba

def create_app() -> FastAPI:
    # 1. Configurar Infraestructura (Base de datos)
    db_conn = get_sqlite_connection()
    
    # 2. Instanciar Adaptadores
    repo = SQLiteRepository(db_conn)
    
    # 3. Instanciar Caso de Uso (Aplicación) inyectando el repositorio
    use_case = CrearFacturaUseCase(repository=repo)
    
    # 4. Inyectar Caso de Uso en el Controlador (Adaptador)
    set_use_case(use_case)
    
    # 5. Configurar Framework (Infraestructura)
    app = FastAPI(title="Sistema de Facturación - Arquitectura Limpia")
    app.include_router(router)
    
    @app.on_event("startup")
    async def startup_event():
        asyncio.create_task(ejecutar_autoprueba())
        
    return app

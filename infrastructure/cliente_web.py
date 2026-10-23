import asyncio
import httpx

async def ejecutar_autoprueba():
    """Cliente HTTP / Web (Autoprueba)"""
    await asyncio.sleep(2)
    print("\n" + "="*40)
    print("=== INICIANDO AUTOPRUEBA HTTP (CLIENTE WEB) ===")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://127.0.0.1:8000/facturas/", 
                json={"cliente": "Cliente Autoprueba", "monto": 500.0}
            )
            print(f"STATUS: {response.status_code}")
            print(f"RESPONSE: {response.json()}")
        except Exception as e:
            print(f"ERROR: {e}")
    print("="*40 + "\n")

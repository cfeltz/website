import asyncio
import fastapi
import uvicorn

from website import api

app = fastapi.FastAPI(lifespan=api.lifespan)
app.include_router(api.ROUTER)

async def main():
    uvicorn_config = uvicorn.Config(app, host='0.0.0.0', port='8080')
    server = uvicorn.Server(uvicorn_config)
    await server.serve()

if __name__ == '__main__':
    asyncio.run(main())
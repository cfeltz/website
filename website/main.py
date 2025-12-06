import asyncio
import fastapi
import os
import uvicorn

from fastapi import staticfiles

from website import api


app = fastapi.FastAPI(lifespan=api.lifespan)
app.include_router(api.ROUTER)
app.mount('/static', staticfiles.StaticFiles(directory=os.path.join(os.getcwd(), 'website/static')), name='static')


async def main():
    uvicorn_config = uvicorn.Config(app, host='0.0.0.0', port=8080)
    server = uvicorn.Server(uvicorn_config)
    await server.serve()

if __name__ == '__main__':
    asyncio.run(main())
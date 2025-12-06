import contextlib
import fastapi

from fastapi import templating

from website.api import root


ROUTER = fastapi.APIRouter()

@contextlib.asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    yield

root.register_route(ROUTER)

import fastapi
import os

from fastapi import templating


ROUTER = fastapi.APIRouter()
TEMPLATES = templating.Jinja2Templates(directory=os.path.join(os.getcwd(), 'website/templates'))

async def root(request: fastapi.Request):
    return TEMPLATES.TemplateResponse(request=request, name='index.html')

def register_route(router: fastapi.APIRouter):
    router.add_api_route('/', root, methods=['GET'], response_class=fastapi.responses.HTMLResponse)


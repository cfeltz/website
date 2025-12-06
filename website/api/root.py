import fastapi

ROUTER = fastapi.APIRouter()

async def root():
    content = """
    <html>
        <body>
            <h1>Hello from Chris Feltz!</h1>
        </body>
    </html>
    """
    return content

def register_route(router: fastapi.APIRouter):
    router.add_api_route('/', root, methods=['GET'], response_class=fastapi.responses.HTMLResponse)


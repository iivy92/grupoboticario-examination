from fastapi import FastAPI
from src.routers import users


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(users.router_v1)
    return app

app = create_app()







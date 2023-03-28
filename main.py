from fastapi import FastAPI
from src.routers import users, items


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(users.router_user_v1)
    app.include_router(items.router_item_v1)
    return app

app = create_app()

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.schemas.user import *
from src.usecases.users import UserUseCases
from http import HTTPStatus

router_v1 = APIRouter(prefix='/v1/user')

@router_v1.post('/signup', status_code=HTTPStatus.CREATED.value)
async def signup_user(user: User) -> UserCreated:
    user_created = await UserUseCases().signup(user)
    return JSONResponse(user_created.dict(), status_code=HTTPStatus.CREATED.value)
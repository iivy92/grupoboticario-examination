from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.schemas.user import *
from src.services.users import UserService
from http import HTTPStatus

router_v1 = APIRouter(prefix='/v1/user')

@router_v1.post('/signup', status_code=HTTPStatus.CREATED.value, response_model=UserCreated)
async def signup_user(user: User) -> JSONResponse:
    user_created = await UserService().signup(user)
    return JSONResponse(user_created.dict(), status_code=HTTPStatus.CREATED.value)
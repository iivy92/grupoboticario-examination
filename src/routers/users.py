from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.schemas.user import *
from src.services.users import UserService
from http import HTTPStatus
from fastapi.security import OAuth2PasswordRequestForm

router_v1 = APIRouter(prefix='/v1/user')

@router_v1.post('/signup', status_code=HTTPStatus.CREATED.value, response_model=UserCreated)
async def signup_user(user: User) -> JSONResponse:
    user_created = await UserService().signup(user)
    return JSONResponse(user_created.dict(), status_code=HTTPStatus.CREATED.value)

@router_v1.post('/signin', status_code=HTTPStatus.OK.value)
async def signin_user(user_credentials: OAuth2PasswordRequestForm = Depends())-> JSONResponse:
    token_jwt = await UserService().signin(user_credentials)
    return JSONResponse(token_jwt.dict(), status_code=HTTPStatus.OK.value)
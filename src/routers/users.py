from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.domain.user import User
from src.usecases.users import UserUseCases

router_v1 = APIRouter(prefix='/v1/user')

@router_v1.post('/signup')
async def signup_user(user: User):
    user_created = await UserUseCases().signup(user)
    return JSONResponse(user_created)
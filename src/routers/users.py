from fastapi import APIRouter
from src.domain.user import User

router_v1 = APIRouter(prefix='v1/user')

@router_v1.post('/signup')
async def signup_user(user: User):
    return user
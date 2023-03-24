from fastapi import APIRouter
from src.models.user import User

router = APIRouter()

@router.post('/user/create')
async def create_user(user: User):
    return user
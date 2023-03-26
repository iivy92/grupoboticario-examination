from fastapi import HTTPException
from http import HTTPStatus

from src.repository.connection import DatabaseConnection
from src.repository.operations import SqlAlchemyRepository
from src.schemas.user import *
from src.repository import models


class UserUseCases:
    def __init__(self):
        self._session = DatabaseConnection()
        self._repository = SqlAlchemyRepository(self._session)
    
    async def signup(self, user: User) -> UserCreated:
        _user = self._repository.get_user_by_cpf(user)
        
        if _user:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value, 
                detail="User already registered"
            )
        
        user_created = self._repository.add(models.User(**user.dict()))
        return UserCreated(**user_created.__dict__)

        

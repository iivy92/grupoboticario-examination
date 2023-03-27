from fastapi import HTTPException
from http import HTTPStatus

from src.repository.connection import DatabaseConnection
from src.repository.operations import SqlAlchemyRepository
from src.schemas.user import *
from src.repository import models
from src.utils.authenticator import Authenticator
from fastapi.security import OAuth2PasswordRequestForm


class UserService:
    def __init__(self):
        self._session = DatabaseConnection()
        self._repository = SqlAlchemyRepository(self._session)
        self._authenticator = Authenticator()
    
    async def signup(self, user: User) -> UserCreated:
        _user = self._repository.get_user_by_cpf(user)
        
        if _user:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value, 
                detail="User already registered"
            )
        
        user_created = self._repository.add(models.User(**user.dict()))
        return UserCreated(**user_created.__dict__)

    async def signin(self, user_login: OAuth2PasswordRequestForm) -> UserCreated:
        user_from_db = self._repository.get_user_by_cpf(user)
        
        if not user_from_db:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value, 
                detail="User does not exist"
            )
        
        if not self._authenticator.verify_hashed_password(plain_password=user.password, hashed_password=user_from_db.password):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED.value, 
                detail="Invalid Credentials"
            )
        
        user_created = self._repository.add(models.User(**user.dict()))
        return UserCreated(**user_created.__dict__)

        

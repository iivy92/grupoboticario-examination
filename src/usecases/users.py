from fastapi import Depends

from src.repository.connection import DatabaseConnection
from src.repository.operations import SqlAlchemyRepository
from src.domain.user import User
from src.repository.models import Users


class UserUseCases:
    def __init__(self):
        self._session = DatabaseConnection()
        self._repository = SqlAlchemyRepository(self._session)
    
    async def signup(self, user: User):
        _user = self._repository.get_user_by_cpf(user)
        if _user:
            # TODO: raise exception for user already exist
            pass
        
        _user = Users(user)
        self._repository.add(_user)
        return _user

        

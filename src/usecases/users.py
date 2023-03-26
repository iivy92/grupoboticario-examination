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

        # TODO: verificar se usuario ja existe
        # TODO: se nao existir incluir no banco
        pass
        

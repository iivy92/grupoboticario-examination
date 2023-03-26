from fastapi import Depends
from sqlalchemy.orm import sessionmaker, Session

from src.repository.connection import DatabaseConnection

class UserUseCases:
    def __init__(self):
        self._session = DatabaseConnection()
    
    def db_session(self):
        self._session.database_session()
    
    async def signup(self, db_session: Session = Depends(db_session)):

        # TODO: verificar se usuario ja existe
        # TODO: se nao existir incluir no banco
        pass
        

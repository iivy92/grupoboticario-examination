from datetime import datetime
from http import HTTPStatus

from fastapi import HTTPException

from src.repository import models
from src.repository.connection import DatabaseConnection
from src.repository.operations import SqlAlchemyRepository
from src.schemas.user import UserCreated
from src.schemas.item import CreateItem, CreatedItem


class ItemService:
    def __init__(self):
        self._session = DatabaseConnection()
        self._repository = SqlAlchemyRepository(self._session)

    async def create_item(self, item: CreateItem, user: UserCreated):
        create_item = CreateItem(**item.dict(), user_cpf=user.cpf)
        item_created = self._repository.add(models.Item(**create_item.dict()))
        return CreatedItem(**item_created.__dict__)

from datetime import datetime
from http import HTTPStatus
import datetime

from fastapi import HTTPException

from src.repository import models
from src.repository.connection import DatabaseConnection
from src.repository.operations import SqlAlchemyRepository
from src.schemas.user import UserCreated
from src.schemas.item import CreateItem, CreatedItem, Items


class ItemService:
    def __init__(self):
        self._session = DatabaseConnection()
        self._repository = SqlAlchemyRepository(self._session)

    async def create_item(self, item: CreateItem, user: UserCreated):
        create_item = CreateItem(**item.dict(), user_cpf=user.cpf)
        item_created = self._repository.add(models.Item(**create_item.dict()))
        return CreatedItem(**item_created.__dict__)

    async def get_items(self, user: UserCreated, date: datetime.date):
        date = datetime.date.today() if date is None else date
        items = self._repository.get_items_by_cpf(user.cpf, date)
        items_list = [CreatedItem(**item.__dict__).dict() for item in items]
        return Items(
            items=items_list,
            total_sales=sum(item["price"] for item in items_list)
        )

    def calculate_bonus(self, items):
        total_sales = sum(item["price"] for item in items)
        
        values = dict(
            total_sales=sum(item["price"] for item in items),
        )



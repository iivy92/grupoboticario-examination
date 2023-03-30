import datetime
from http import HTTPStatus

import requests
from fastapi import HTTPException

from src.repository import models
from src.repository.connection import DatabaseConnection
from src.repository.operations import SqlAlchemyRepository
from src.schemas.item import CreatedItem, CreateItem, Items, ItemsReward
from src.schemas.user import UserCreated


class ItemService:
    def __init__(self):
        self._session = DatabaseConnection()
        self._repository = SqlAlchemyRepository(self._session)

    async def create_item(self, item: CreateItem, user: UserCreated) -> CreatedItem:
        item_from_db = self._repository.get_item_by_code(item.code)
        if item_from_db:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value,
                detail="Item already registered",
            )

        create_item = CreateItem(**item.dict(), user_cpf=user.cpf)
        item_created = self._repository.add(models.Item(**create_item.dict()))
        return CreatedItem(**item_created.__dict__)

    async def get_items(self, user: UserCreated, date: datetime.date) -> Items:
        date = datetime.date.today() if date is None else date
        items = self._repository.get_items_by_cpf(user.cpf, date)
        items_list = [CreatedItem(**item.__dict__).dict() for item in items]

        return Items(
            reward=self.calculate_bonus(items_list),
            items=items_list,
        )

    async def get_accumulated_credit(self) -> ItemsReward:
        url = "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf=12312312323"
        response = requests.get(url)
        return ItemsReward(accumulated=response.json()["body"]["credit"])

    @staticmethod
    def calculate_bonus(items: list) -> dict:
        total_sales = sum(item["price"] for item in items)

        match int(total_sales):
            case total if total in range(0, 1000):
                reward = total * 0.10
                fee = "10%"
            case total if total in range(1000, 1500):
                reward = total * 0.15
                fee = "15%"
            case _:
                reward = total * 0.20
                fee = "20%"

        return dict(total_sales=total_sales, reward=reward, fee=fee)

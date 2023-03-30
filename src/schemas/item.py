from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, root_validator

DEAFAULT_CPF = ["153.509.460-56", "15350946056"]


class Status(str, Enum):
    IN_VALIDATION = "in_validation"
    APPROVED = "approved"


class Item(BaseModel):
    code: str
    date: date
    price: float
    status: Optional[Status]

    class Config:
        use_enum_values = True


class CreateItem(Item):
    user_cpf: str

    class Config:
        validate_assignment = True

    @root_validator(allow_reuse=True)
    def set_status(cls, values):
        if not values["status"]:
            values["status"] = Status.IN_VALIDATION.value

        if values["user_cpf"] in DEAFAULT_CPF:
            values["status"] = Status.APPROVED.value

        return values


class CreatedItem(Item):
    @root_validator
    def set_date(cls, values):
        values["date"] = values["date"].strftime("%Y-%m-%d")
        return values


class ItemsReward(BaseModel):
    total_sales: Optional[float]
    reward: Optional[float]
    fee: Optional[str]
    accumulated: Optional[float]


class Items(BaseModel):
    items: list[CreatedItem]
    reward: ItemsReward

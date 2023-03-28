from datetime import date
from pydantic import BaseModel, root_validator, validator
from typing import Optional
from enum import Enum


class Status(str, Enum):
    IN_VALIDATION = 'in_validation'
    APPROVED = 'approved'

class Item(BaseModel):
    code: str
    date: date
    price: float
    status: Optional[list[Status]]

class CreateItem(Item):
    user_cpf: str
    status: Optional[list[Status]]

    class Config:
        validate_assignment = True

    @root_validator(allow_reuse=True)
    def set_status(cls, values):
        if not values["status"]:
            values["status"] = Status.IN_VALIDATION.value
        if values["user_cpf"] in ["153.509.460-56", "15350946056"]:
            values["status"] = Status.APPROVED.value    
        return values

from src.schemas.item import CreateItem, Status, DEAFAULT_CPF
import pytest
from pydantic.error_wrappers import ValidationError



def test_create_item():
    item = CreateItem(
        code="btc001",
        date="2018-03-27",
        status=Status.APPROVED.value,
        price=345.7,
        user_cpf="03374110509"
    )

    assert item.code == "btc001"

def test_create_item_with_no_status():
    item = CreateItem(
        code="btc001",
        date="2018-03-27",
        price=345.7,
        user_cpf="03374110509"
    )

    assert item.status == Status.IN_VALIDATION.value

def test_create_item_with_default_cpf():
    item = CreateItem(
        code="btc001",
        date="2018-03-27",
        price=345.7,
        user_cpf=DEAFAULT_CPF[0]
    )

    assert item.status == Status.APPROVED.value

def test_create_item_missing_field():
    with pytest.raises(ValidationError):
        CreateItem(
            date="2018-03-27",
            price=345.7,
            user_cpf="03374110509"
        )
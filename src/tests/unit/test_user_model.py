import pytest
from pydantic.error_wrappers import ValidationError

from src.schemas.user import *


def test_create_user():
    user = User(
        name="Pedro Ivo Mendes de Santana",
        cpf="03374110509",
        email="pedro@email.com",
        password="password@123",
    )

    assert user.name == "Pedro Ivo Mendes de Santana"
    assert user.cpf == "03374110509"
    assert user.email == "pedro@email.com"


def test_create_user_missing_field():
    with pytest.raises(ValidationError):
        User(
            name="Pedro Ivo Mendes de Santana",
            email="pedro@email.com",
            password="password@123",
        )


def test_create_user_with_invalid_cpf():
    with pytest.raises(ValidationError):
        User(
            name="Pedro Ivo Mendes de Santana",
            cpf="99999988877",
            email="pedro@email.com",
            password="password@123",
        )


def test_create_user_with_invalid_email():
    with pytest.raises(ValidationError):
        User(
            name="Pedro Ivo Mendes de Santana",
            cpf="99999988877",
            email="pedro##email.com",
            password="password@123",
        )


def test_hashed_password(authenticator):
    _password = "password@123"
    user = User(
        name="Pedro Ivo Mendes de Santana",
        cpf="03374110509",
        email="pedro@email.com",
        password=_password,
    )

    assert authenticator.verify_hashed_password(_password, user.password)


def test_created_user():
    user = UserCreated(
        id=1,
        name="Pedro Ivo Mendes de Santana",
        cpf="03374110509",
        email="pedro@email.com",
    )
    assert user.id == 1
    assert user.name == "Pedro Ivo Mendes de Santana"
    assert user.cpf == "03374110509"
    assert user.email == "pedro@email.com"


def test_user_token():
    token = UserToken(access_token="some-token")
    assert token.access_token == "some-token"

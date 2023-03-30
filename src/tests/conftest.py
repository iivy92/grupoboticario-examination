import pytest
from fastapi.testclient import TestClient
from validate_docbr import CPF
from strgen import StringGenerator

from main import app
from src.utils.authenticator import Authenticator

cpf_validator = CPF()
user_cpf = cpf_validator.generate()

item_code = StringGenerator("[\l\d]{8}").render()


@pytest.fixture
def client():
    client = TestClient(app)
    return client

@pytest.fixture
def authenticator():
    return Authenticator()

@pytest.fixture(scope="session")
def auth_header():
    access_token = Authenticator().generate_jwt_token(user_cpf)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    return headers

@pytest.fixture
def user_signup_payload():
    return {
        "name": "Pedro Ivo",
        "cpf": user_cpf,
        "email": "email@example.com",
        "password": "P@ss1234",
    }


@pytest.fixture
def user_signin_payload():
    return {"username": user_cpf, "password": "P@ss1234"}


@pytest.fixture
def user_signin_invalid_credential():
    return {"username": user_cpf, "password": "P@ss"}


@pytest.fixture
def user_signin_dont_exist():
    return {"username": "78779189504", "password": "P@ss1234"}


@pytest.fixture
def item_created_sucessfully():
    return { 
        "code": item_code,
        "date": "2023-04-28", 
        "price": 134.9,
    }

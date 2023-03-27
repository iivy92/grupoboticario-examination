import pytest
from fastapi.testclient import TestClient
from validate_docbr import CPF

from main import app
from src.repository.models import User
from src.utils.authenticator import Authenticator

cpf_validator = CPF()
user_cpf = cpf_validator.generate()


@pytest.fixture
def client():
    client = TestClient(app)
    return client


@pytest.fixture
def authenticator():
    return Authenticator()


@pytest.fixture(scope="session")
def user_signup_payload():
    return {
        "name": "Pedro Ivo",
        "cpf": user_cpf,
        "email": "email@example.com",
        "password": "P@ss1234",
    }


@pytest.fixture(scope="session")
def user_signin_payload():
    return {"username": user_cpf, "password": "P@ss1234"}


@pytest.fixture(scope="session")
def user_signin_invalid_credential():
    return {"username": user_cpf, "password": "P@ss"}


@pytest.fixture(scope="session")
def user_signin_dont_exist():
    return {"username": "78779189504", "password": "P@ss1234"}

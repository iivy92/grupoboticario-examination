import pytest
from src.utils.hasher import Hasher
from fastapi.testclient import TestClient
from main import app
from src.repository.models import User
from validate_docbr import CPF



@pytest.fixture
def client():
    client = TestClient(app)
    return client

@pytest.fixture
def hasher():
    hasher = Hasher()
    return hasher

@pytest.fixture(scope='session')
def user_signup_payload():
    cpf_validator = CPF()
    return {
        "name": "Pedro Ivo",
        "cpf": cpf_validator.generate(),
        "email": "email@example.com",
        "password": "P@ss1234"
    }

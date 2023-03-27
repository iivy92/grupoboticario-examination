import pytest
from src.utils.hasher import Hasher

@pytest.fixture
def hasher():
    hasher = Hasher()
    return hasher

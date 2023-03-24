import pytest
from pydantic.error_wrappers import ValidationError
from src.models.user import User



def test_create_user():
    user = User(
        name='Pedro Ivo Mendes de Santana',
        cpf='03374110509',
        email='pedro@email.com',
        password='password@123'
    )

    assert user.name == 'Pedro Ivo Mendes de Santana'
    assert user.cpf == '03374110509'
    assert user.email == 'pedro@email.com'
    assert user.password == 'password@123'

def test_create_user_missing_field():
    with pytest.raises(ValidationError):
        User(
            name='Pedro Ivo Mendes de Santana',
            email='pedro@email.com',
            password='password@123'
        )



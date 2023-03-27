import pytest
from http import HTTPStatus


def test_user_singup_successfully(client, user_signup_payload):
    response = client.post('/v1/user/signup', json=user_signup_payload)
    assert response.status_code == HTTPStatus.CREATED.value

def test_user_already_exists(client, user_signup_payload):
    response = client.post('/v1/user/signup', json=user_signup_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST.value
    assert response.text == '{"detail":"User already registered"}'
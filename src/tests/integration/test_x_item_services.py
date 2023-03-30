from http import HTTPStatus
import pytest

def test_create_item_successfully(client, item_created_sucessfully, auth_header):
    response = client.post("/v1/items/create", json=item_created_sucessfully, headers=auth_header)
    assert response.status_code == HTTPStatus.CREATED.value

def test_create_item_already_exist(client, item_created_sucessfully, auth_header):
    response = client.post("/v1/items/create", json=item_created_sucessfully, headers=auth_header)
    assert response.status_code == HTTPStatus.BAD_REQUEST.value
    assert response.text == '{"detail":"Item already registered"}'


# def test_user_already_exists(client, user_signup_payload):
#     response = client.post("/v1/user/signup", json=user_signup_payload)
#     assert response.status_code == HTTPStatus.BAD_REQUEST.value
#     assert response.text == '{"detail":"User already registered"}'


# def test_user_singin_successfully(client, user_signin_payload):
#     response = client.post("/v1/user/signin", data=user_signin_payload)
#     assert response.status_code == HTTPStatus.OK.value


# def test_user_singin_invalid_credentiasl(client, user_signin_invalid_credential):
#     response = client.post("/v1/user/signin", data=user_signin_invalid_credential)
#     assert response.status_code == HTTPStatus.UNAUTHORIZED.value
#     assert response.text == '{"detail":"Invalid Credentials"}'


# def test_user_doesnot_exist(client, user_signin_dont_exist):
#     response = client.post("/v1/user/signin", data=user_signin_dont_exist)
#     assert response.status_code == HTTPStatus.BAD_REQUEST.value
#     assert response.text == '{"detail":"User does not exist"}'

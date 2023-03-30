from http import HTTPStatus


def test_create_item_successfully(client, item_created_sucessfully, auth_header):
    response = client.post(
        "/v1/items/create", json=item_created_sucessfully, headers=auth_header
    )
    assert response.status_code == HTTPStatus.CREATED.value


def test_create_item_already_exist(client, item_created_sucessfully, auth_header):
    response = client.post(
        "/v1/items/create", json=item_created_sucessfully, headers=auth_header
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST.value
    assert response.text == '{"detail":"Item already registered"}'


def test_search_items_by_cpf(client, auth_header):
    response = client.get("/v1/items/search", headers=auth_header)
    assert response.status_code == HTTPStatus.OK.value

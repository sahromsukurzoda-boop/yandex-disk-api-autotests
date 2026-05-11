def test_get_resources(api):

    response = api.get_resources()

    assert response.status_code == 200

    body = response.json()

    assert "_embedded" in body
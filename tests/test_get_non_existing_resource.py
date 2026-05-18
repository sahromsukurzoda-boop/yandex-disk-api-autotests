def test_get_non_existing_resource(api):

    response = api.get_resource("not_existing_resource")

    assert response.status_code == 404
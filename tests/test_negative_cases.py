def test_delete_non_existing_resource(api):

    response = api.delete_resource("not_existing_folder")

    assert response.status_code == 404
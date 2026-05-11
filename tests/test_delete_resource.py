import uuid


def test_delete_resource(api):

    folder_name = f"folder_to_delete_{uuid.uuid4()}"

    create_response = api.create_folder(folder_name)

    assert create_response.status_code == 201

    delete_response = api.delete_resource(folder_name)

    assert delete_response.status_code in [202, 204]
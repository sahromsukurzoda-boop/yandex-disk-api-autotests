import uuid


def test_create_folder(api):

    folder_name = f"test_folder_{uuid.uuid4()}"

    response = api.create_folder(folder_name)

    assert response.status_code == 201
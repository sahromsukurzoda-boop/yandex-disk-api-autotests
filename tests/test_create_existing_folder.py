import uuid
import time


def test_create_existing_folder(api):

    folder_name = f"folder_{uuid.uuid4()}"

    first_response = api.create_folder(folder_name)

    assert first_response.status_code == 201

    time.sleep(1)

    second_response = api.create_folder(folder_name)

    assert second_response.status_code == 409
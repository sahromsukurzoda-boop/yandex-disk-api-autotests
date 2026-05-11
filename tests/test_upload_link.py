import uuid


def test_get_upload_link(api):

    file_name = f"test_file_{uuid.uuid4()}.txt"

    response = api.get_upload_link(file_name)

    assert response.status_code == 200

    body = response.json()

    assert "href" in body
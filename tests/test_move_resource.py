import uuid


def test_move_resource(api):

    source_folder = f"source_{uuid.uuid4()}"
    target_folder = f"target_{uuid.uuid4()}"

    create_response = api.create_folder(source_folder)

    assert create_response.status_code == 201

    move_response = api.move_resource(
        source_folder,
        target_folder
    )

    assert move_response.status_code in [201, 202]
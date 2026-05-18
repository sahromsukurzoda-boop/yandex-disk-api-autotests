import uuid
import time
import requests


def test_move_non_existing_resource(api):

    target_folder = f"target_{uuid.uuid4()}"

    time.sleep(1)

    try:
        response = api.move_resource(
            "not_existing_resource",
            target_folder
        )

        assert response.status_code == 404

    except requests.exceptions.ConnectionError:
        pass
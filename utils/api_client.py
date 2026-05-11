import requests

from utils.config import TOKEN, BASE_URL


class DiskAPI:

    def __init__(self):
        self.headers = {
            "Authorization": f"OAuth {TOKEN}"
        }

    def get_resources(self):
        return requests.get(
            BASE_URL,
            headers=self.headers,
            params={"path": "/"}
        )

    def create_folder(self, path):
        return requests.put(
            BASE_URL,
            headers=self.headers,
            params={"path": path}
        )

    def get_upload_link(self, path):
        return requests.get(
            f"{BASE_URL}/upload",
            headers=self.headers,
            params={
                "path": path,
                "overwrite": "true"
            }
        )

    def delete_resource(self, path):
        return requests.delete(
            BASE_URL,
            headers=self.headers,
            params={
                "path": path,
                "permanently": "true"
            }
        )
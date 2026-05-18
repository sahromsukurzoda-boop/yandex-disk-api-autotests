import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class DiskAPI:
    BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
    TIMEOUT = 30
    
    def __init__(self, token):
        self.headers = {
            "Authorization": f"OAuth {token}"
        }

        self.session = requests.Session()

        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "PUT", "POST", "DELETE"]
        )

        adapter = HTTPAdapter(max_retries=retries)

        self.session.mount("https://", adapter)

    def create_folder(self, path):
        return self.session.put(
            self.BASE_URL,
            headers=self.headers,
            params={"path": path},
            timeout=self.TIMEOUT
        )

    def get_resource(self, path):
        return self.session.get(
            self.BASE_URL,
            headers=self.headers,
            params={"path": path},
            timeout=self.TIMEOUT
    )

    def get_resources(self):
        return self.session.get(
            self.BASE_URL,
            headers=self.headers,
            params={"path": "/"},
            timeout=self.TIMEOUT
    )

    def delete_resource(self, path):
        return self.session.delete(
            self.BASE_URL,
            headers=self.headers,
            params={
                "path": path,
                "permanently": "true"
            },
            timeout=self.TIMEOUT
        )

    def move_resource(self, from_path, to_path):
        return self.session.post(
            f"{self.BASE_URL}/move",
            headers=self.headers,
            params={
                "from": from_path,
                "path": to_path
            },
            timeout=self.TIMEOUT
        )

    def get_upload_link(self, path):
        return self.session.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            headers=self.headers,
            params={"path": path},
            timeout=self.TIMEOUT
        )
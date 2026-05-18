import os
import pytest

from dotenv import load_dotenv
from utils.api_client import DiskAPI

load_dotenv()


@pytest.fixture
def api():
    token = os.getenv("YANDEX_TOKEN")

    return DiskAPI(token)
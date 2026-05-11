import pytest

from utils.api_client import DiskAPI


@pytest.fixture
def api():
    return DiskAPI()
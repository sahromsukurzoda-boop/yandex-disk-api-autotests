from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("YANDEX_TOKEN")

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
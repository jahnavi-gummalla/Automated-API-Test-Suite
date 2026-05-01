import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def session():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    return s


@pytest.fixture
def timeout():
    return TIMEOUT

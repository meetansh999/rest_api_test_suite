# import pytest

# @pytest.fixture(scope = "session")
# def base_url():
#     return "https://jsonplaceholder.typicode.com"


import os, pytest

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")

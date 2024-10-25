# tests/conftest.py
import pytest
from faker import Faker # type: ignore

@pytest.fixture(scope="function")
def fake_data():
    faker = Faker()
    return faker
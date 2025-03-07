import faker
import pytest


@pytest.fixture
def email() -> str:
    return faker.Faker().email()


@pytest.fixture
def password() -> str:
    return faker.Faker().password()


@pytest.fixture
def first_name() -> str:
    return faker.Faker().first_name()


@pytest.fixture
def last_name() -> str:
    return faker.Faker().last_name()


@pytest.fixture
def full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


@pytest.fixture
def access_token() -> str:
    return faker.Faker().password()


@pytest.fixture
def refresh_token() -> str:
    return faker.Faker().password()

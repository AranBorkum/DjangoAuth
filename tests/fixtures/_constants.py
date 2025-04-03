from random import randint
from uuid import UUID, uuid4

import jwt
from faker import Faker
from pytest import fixture


@fixture
def first_name() -> str:
    return Faker().first_name()


@fixture
def last_name() -> str:
    return Faker().last_name()


@fixture
def full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


@fixture
def email() -> str:
    return Faker().email()


@fixture
def password() -> str:
    return Faker().password()


@fixture
def user_id() -> UUID:
    return uuid4()


@fixture
def one_time_password() -> str:
    return "".join(str(randint(0, 9)) for _ in range(6))


@fixture
def token() -> str:
    return str(jwt.encode(payload={}, key="key"))

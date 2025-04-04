import random
import string
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


@fixture
def billing_address_id() -> UUID:
    return uuid4()


@fixture
def shipping_address_id() -> UUID:
    return uuid4()


@fixture
def line1() -> str:
    return Faker("en_US").street_address()


@fixture
def line2() -> str:
    return ""


@fixture
def city() -> str:
    return Faker("en_US").city()


@fixture
def state() -> str:
    return Faker("en_US").state()


@fixture
def country() -> str:
    return Faker("en_US").current_country()


@fixture
def postal_code() -> str:
    return Faker("en_US").postcode()


@fixture
def customer_id() -> str:
    random_sample = "".join([
        str(random.sample(string.ascii_lowercase + string.digits, 1)[0])
        for _ in range(10)
    ])
    return f"cus_{random_sample}"


@fixture
def product_name() -> str:
    return Faker("en_US").cryptocurrency_name()


@fixture
def product_id() -> str:
    random_sample = "".join([
        str(random.sample(string.ascii_lowercase + string.digits, 1)[0])
        for _ in range(10)
    ])
    return f"prod_{random_sample}"

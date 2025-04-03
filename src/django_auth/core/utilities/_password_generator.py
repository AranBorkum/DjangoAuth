from random import randint


def otp_password_generator() -> str:
    return "".join(str(randint(0, 9)) for _ in range(6))

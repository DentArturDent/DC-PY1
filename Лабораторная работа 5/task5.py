from random import sample
import string


def get_random_password(n: int) -> str:
    password = ''.join(sample(string.ascii_letters + string.digits, n))

    return password


print(get_random_password(8))

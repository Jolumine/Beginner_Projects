import random
import string

ELEMENTS = f"{string.ascii_lowercase}{string.ascii_uppercase}{string.digits}!§$%&/()=?€@"

def generate(length:int):
    password = ""
    for i in range(length):
        password+=random.choice(ELEMENTS)

    return password


def generate_2(length:int) -> str: 
    return "".join([random.choice(ELEMENTS) for i in range(length)])


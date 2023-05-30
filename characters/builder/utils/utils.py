from uuid import uuid4


def generate_id():
    new_id = str(uuid4())
    return new_id

import uuid

def get_random_uuid() -> str:
    # generate random UUID
    return str(uuid.uuid4())

uuid_value = get_random_uuid()


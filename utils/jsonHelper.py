import jsonpickle


def encode(val: object) -> str:
    return jsonpickle.encode(val)


def decode(val: str) -> object:
    return jsonpickle.decode(val)

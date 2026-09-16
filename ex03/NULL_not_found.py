import math


def NULL_not_found(object: any) -> int:
    """Print the type of every kind of "Null" value.

    Recognises None, NaN, zero, empty string and False. Returns 0 when a
    known "Null" value is handled, 1 otherwise.
    """
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0

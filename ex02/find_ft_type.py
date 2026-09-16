def all_thing_is_obj(object: any) -> int:
    """Print the type of the given object and always return 42.

    Known containers (list, tuple, set, dict) are announced by name,
    strings are located "in the kitchen", anything else is not found.
    """
    named = {list: "List", tuple: "Tuple", set: "Set", dict: "Dict"}
    obj_type = type(object)
    if obj_type in named:
        print(f"{named[obj_type]} : {obj_type}")
    elif obj_type is str:
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not Found")
    return 42

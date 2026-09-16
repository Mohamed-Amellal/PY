import sys


def main():
    """Read one integer from argv and tell whether it is odd or even."""
    args = sys.argv[1:]
    if len(args) == 0:
        return
    assert len(args) == 1, "more than one argument are provided"
    try:
        number = int(args[0])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")

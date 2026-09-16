import sys
from ft_filter import ft_filter


def main():
    """Print words of a string S whose length is strictly greater than N."""
    args = sys.argv[1:]
    assert len(args) == 2, "the arguments are bad"
    text = args[0]
    try:
        length = int(args[1])
    except ValueError:
        raise AssertionError("the arguments are bad")
    assert isinstance(text, str), "the arguments are bad"
    words = ft_filter(lambda word: len(word) > length, text.split(" "))
    print([word for word in words])


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")

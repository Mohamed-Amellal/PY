import sys
import string


def analyze(text):
    """Count and display character categories inside the given text."""
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    punctuation = sum(1 for char in text if char in string.punctuation)
    spaces = sum(1 for char in text if char.isspace())
    digits = sum(1 for char in text if char.isdigit())
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Get a string from argv or from a prompt, then analyze it."""
    args = sys.argv[1:]
    assert len(args) <= 1, "more than one argument are provided"
    if len(args) == 1:
        text = args[0]
    else:
        text = input("What is the text to count?\n") + "\n"
    analyze(text)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")

import time
from datetime import datetime


def main():
    """Print the seconds since the epoch and today's date, formatted."""
    now = time.time()
    print(
        "Seconds since January 1, 1970: "
        "{:,.4f} or {:.2e} in scientific notation".format(now, now)
    )
    print(datetime.now().strftime("%b %d %Y"))


if __name__ == "__main__":
    main()

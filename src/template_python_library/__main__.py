"""A CLI example for the library."""

import sys

from . import add


def main() -> None:
    """Perform a simple addition and print the result."""
    result = add(1, 2)
    sys.stdout.write(f"1 + 2 = {result}\n")


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""this module defines a function that print a
square with #
"""


def print_square(size):
    """
    Print a square with the character #.

    Args:
        size (int): Length of the square.

    Raises:
        TypeError: If size is not an integer
        or if size is a float and less than zero.
        ValueError: If size is less than zero.
    """

    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be a non-negative integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

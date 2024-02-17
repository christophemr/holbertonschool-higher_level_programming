#!/usr/bin/python3
"""This module defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file
    """
    # Open the file in append mode with UTF-8 encoding
    with open(filename, "a", encoding="utf-8") as f:
        # Append the provided text to the end of the file
        # and return the number of characters appended
        return f.write(text)

#!/usr/bin/python3
"""This module defines a file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file
    """
    # Open the file in write mode with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        # Write the provided text to the file and return
        # the number of characters written
        return f.write(text)

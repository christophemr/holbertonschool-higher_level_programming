#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file"""
    # open the file in read mode with UTF-8 encoding
    with open(filename, encoding="utf-8") as f:
        # Read and print the contents of the file
        print(f.read(), end="")

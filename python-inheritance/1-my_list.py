#!/usr/bin/python3
"""This module defines the mylist class"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))

#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.
        """
        if (attrs is not None and isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        return self.__dict__

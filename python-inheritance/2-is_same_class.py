#!/usr/bin/python3
"""Checks if object is an instance of the specified class"""


def is_same_class(obj, a_class):
    """Return true if object is an instance of the
    specified class, otherwise return false
    """
    return (type(obj) == a_class)

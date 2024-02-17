#!/usr/bin/python3
"""This module defines a JSON-to-object function"""


import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string.

    Args:
        my_str (str): The JSON-formatted string to be converted.

    Returns:
        Any: The Python object representation of the input JSON string
    """
    """Returns the Python object representation of a JSON string"""
    # Use the json.loads() function to convert the JSON-formatted
    # string to a Python object
    return json.loads(my_str)

#!/usr/bin/python3
"""This module creates an object from a JSON file"""

import json


def load_from_json_file(filename):
    """Load data from a JSON file and return the
    corresponding Python object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object created from the JSON data.
    """
    with open(filename, "r") as file:
        return json.load(file)

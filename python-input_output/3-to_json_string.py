#!/usr/bin/python3
"""This module defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object"""
    # Use the json.dumps() function to convert the Python
    # object to a JSON-formatted string
    return json.dumps(my_obj)

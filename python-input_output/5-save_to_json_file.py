#!/usr/bin/python3
"""this module define a JSON representation that
writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file"""
    with open(filename, "w",) as f:
        json.dump(my_obj, f)

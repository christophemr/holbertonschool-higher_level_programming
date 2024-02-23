#!/usr/bin/python3
"""This module defines the base class to serve for the other classes"""


import csv
import json
import os
import turtle


class Base:
    """Represents base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries."""

        # Check if list_dictionaries is None or empty
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        # Check if list_dictionaries is a list of dictionaries
        if (type(list_dictionaries) is list or not
                all(isinstance(i, dict) for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")

        # Convert list_dictionaries to JSON string and return
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file."""

        # Construct the file name based on the class name
        file_name = cls.__name__ + ".json"

        # Open the file for writing
        with open(file_name, "w") as jsonfile:

            # Check if the list of objects is None
            if list_objs is None:
                jsonfile.write("[]")
            else:
                # Convert the list of objects to a list of dictionaries
                list_dicts = [obj.to_dictionary() for obj in list_objs]

            # Write the JSON representation of the list
            # of dictionaries to the file
            jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of objects."""

        # Initialize an empty list to store JSON string representations
        json_string_list = []

        # Check if json_string is not None and not an empty string
        if json_string is not None and json_string != '':

            # Check if json_string is a string
            if not isinstance(json_string, str):
                raise TypeError("json_string must be a string")

            # Parse the JSON string and store the result in json_string_list
            json_string_list = json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        # create a dummy instance based on
        # existing class type
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            raise Exception("Wrong class")
        # Update the attributes of the dummy instance
        # using the provided dictionary
        dummy.update(**dictionary)
        # Return the populated dummy instance
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads instances from a JSON file and returns a list of instances."""

        # Construct the file name based on the class name
        file_name = cls.__name__ + ".json"

        # Initialize lists to store instances and dictionaries
        list_of_instances = []
        list_dictionaries = []

        # Check if the file exists
        if os.path.exists(file_name):
            # Read the content of the file
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()

            # Convert the JSON string to a list of dictionaries
            list_dictionaries = cls.from_json_string(my_str)

            # Create instances from the dictionaries and add them to the list
            for dictionary in list_dictionaries:
                list_of_instances.append(cls.create(**dictionary))

        # Return the list of instances
        return list_of_instances

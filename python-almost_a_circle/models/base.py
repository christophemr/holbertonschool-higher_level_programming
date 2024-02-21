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

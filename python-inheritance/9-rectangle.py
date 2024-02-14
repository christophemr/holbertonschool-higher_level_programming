#!/usr/bin/python3
"""defines a Rectangle inherited from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns a human-readable representation of a Rectangle."""

    # Get the name of the class using __class__.__name__
        class_name = self.__class__.__name__

    # Create a string representing the width and height of the rectangle
        dimensions = f"{self.__width}/{self.__height}"

    # Combine class name, brackets, and dimensions into a formatted string
        result_string = f"[{class_name}] {dimensions}"
    # Return the formatted string as the representation of the Rectangle
        return result_string

#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
# Import the Rectangle class from module '9-rectangle'
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new square with a given size.

        Args:
            size (int): The size of the square.
        """
        # Call the integer_validator method from the parent class to validate the size
        self.integer_validator("size", size)

        # Call the __init__ method of the parent class (Rectangle) with size for both width and height
        super().__init__(size, size)

        # Set the size attribute for the Square object
        self.__size = size

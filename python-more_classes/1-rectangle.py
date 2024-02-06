#!/usr/bin/python3
"""
define Rectangle class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """initialization of the rectangle class

        Args:
            width : represent the width of the rectangle
            height : represent the height of the rectangle

        Raises:
            TypeError: if width is not an integre
            ValueError: if width is less than 0
        """
        self.height = height
        self.width = width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("size must be >= 0")
        self.__width = width

    @property
    def width(self):
        """setter method for retrieving the rectangle size"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter method for setting the rectangle size

        Args:
            value : the new size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method retrieving the  rectangle size"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method for setting the square size

        Args:
            value : height value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

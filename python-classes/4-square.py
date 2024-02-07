#!/usr/bin/python3
"""defines a square class"""


class Square:
    """
        represents a square class
    """

    def __init__(self, size=0):
        """intializing the square class


        Args:
            size (int): represent the size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter method for retrieving the square size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for setting the square size

        Args:
            value (int): the new size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            measure the area
            return: the current square area
        """
        return (self.__size ** 2)

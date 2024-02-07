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
              Defaults to 0.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            measure the area
            return: the current square area
        """
        return (self.__size ** 2)

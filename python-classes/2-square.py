#!/usr/bin/python3

class Square:
    """
        defines a square class
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
            raise TypeError("must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

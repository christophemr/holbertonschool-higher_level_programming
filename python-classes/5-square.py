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
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            measure the area
            return: the current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """use the # to print the square
        """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)

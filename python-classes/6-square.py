#!/usr/bin/python3
"""defines a square class"""


class Square:
    """
        represents a square class
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
        """intializing the square class with size and position


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

    @property
    def position(self):
        """Getter method for retrieving the position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """validate and set the position of the square
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """use the # to print the square
        """
        if self.__size == 0:
            print()
        else:
            """print new line characters for vertical position
            """
            for _ in range(self.__position[1]):
                print()
                """print the square using the '#'
                   characters and horizontal position
                """
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

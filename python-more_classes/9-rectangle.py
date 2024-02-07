#!/usr/bin/python3
"""
define Rectangle class
"""


class Rectangle:
    """represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        """initialization of the rectangle class

        Args:
            width : represents the width of the rectangle
            height : represents the height of the rectangle

        Raises:
            TypeError: if width is not an integre
            ValueError: if width is less than 0
        """

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

    def area(self):
        """returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """represent diagram of rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        Rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    Rectangle += str(self.print_symbol)
                except Exception:
                    Rectangle += type(self).print_symbol
            if column < self.__height - 1:
                Rectangle += "\n"
        return (Rectangle)
    """string representation of the rectangle"""

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """print a message when an instance of rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the grater area

        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new rectangle with width and height equal to size

        Args:
            size (int): The width and height of the new rectangle
        """
        return cls(size, size)

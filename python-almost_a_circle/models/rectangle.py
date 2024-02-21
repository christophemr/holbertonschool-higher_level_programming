#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the value for width"""
        return (self.__width)

    @property
    def height(self):
        """gets the value for height"""
        return (self.__height)

    @property
    def x(self):
        """gets the value for x"""
        return (self.__x)

    @property
    def y(self):
        """gets the value for y"""
        return (self.__y)

    @width.setter
    def width(self, value):
        """sets the value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the value for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """sets the value for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """sets the value for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """displays the rectangle using #"""
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            # print leading spaces
            print(" " * self.x, end="")

            print("#" * self.__width)

    def __str__(self):
        """defines a format for the string
        representation of the class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns arguments to attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, attributes[i], value) if value is not\
                None else None
        for key, value in kwargs.items():
            setattr(self, key, value) if value is not\
                None else None

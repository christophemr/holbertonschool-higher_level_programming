#!/usr/bin/python3
"""This module contains a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        # Call the super() constructor with the necessary arguments
        super().__init__(size, size, x, y, id)
        # Set size attribute directly to avoid confusion
        self.size = size

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Gets the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        # Set both width and height to the same value
        self.__width = self.__height = value

    def update(self, *args, **kwargs):
        """Updates attributes of an instance"""
        if args:
            # If args is not empty
            arg_names = ['id', 'size', 'x', 'y']
            # Use min() to prevent IndexError if args is shorter than arg_names
            for i, arg_value in enumerate(args[:len(arg_names)]):
                setattr(self, arg_names[i], arg_value)
        else:
            # If args is empty, update based on keyword arguments
            for key, value in kwargs.items():
                if key in ('id', 'size', 'x', 'y'):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

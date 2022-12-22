#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a Square."""

    def __init__(self, size=0):
        """Initialize the Square

        Args:
            size (int): size of the new squar.
        """

        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        size = self.__size
        return size * size

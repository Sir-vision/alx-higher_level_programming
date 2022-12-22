#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a Square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new Square.
        """

        self.__size = size

    @property
    def size(self):
        """get/set the current size of the new Square."""

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Return the current area of the Square."""
        return self.__size ** 2

    def my_print(self):
        """Print the Square with the # character"""

        size = self.__size

        if size == 0:
            print()

        for row in range(size):
            print('#' * size)

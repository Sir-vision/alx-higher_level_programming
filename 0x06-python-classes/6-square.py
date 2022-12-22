#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """get/set the current size of the Square"""

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """get/set the current position of the Square"""

        return self.__position

    @position.setter
    def position(self, value):
        message = 'position must be a tuple of 2 positive integers'
        if type(value) != tuple or len(value) != 2:
            raise TypeError(message)

        for items in value:
            if type(items) != int or items < 0:
                raise TypeError(message)

        self.__position = value

    def area(self):
        """Return the current area of the Square"""

        return self.__size ** 2

    def my_print(self):
        """Print the Square with a # character"""

        size = self.__size
        nl = self.__position[1]
        ws = self.__position[0]

        if size == 0:
            print()

        for newlines in range(nl):
            print()

        for row in range(size):
            print((' ' * ws) + ('#' * size))

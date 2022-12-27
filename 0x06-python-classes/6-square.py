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
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        i, j = value
        if not isinstance(i, int) or not isinstance(j, int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if (i < 0) or (j < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return the current area of the Square"""

        return pow(self.__size, 2)

    def my_print(self):
        """Print the Square with a # character"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(pow(self.__size, 2)):
                if (i % self.__size == 0):
                    if i != 0:
                        print()
                    for j in range(self.__position[0]):
                        print(" ", end='')
                print('#', end='')
            print()

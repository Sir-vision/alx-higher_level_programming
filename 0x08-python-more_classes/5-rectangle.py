#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """Represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of the new rectangle.
        Args:
            width (int): The width of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """get/set the current width of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """get/set the current height of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Area of Rectangle (width * height)"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of a Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ print() __str__ method funtion to return rectangle in char '#'
        """
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res

        for i in range(self.__height):
            if i == self.__height - 1:
                res += ('#' * self.__width)
            else:
                res += (('#' * self.__width) + '\n')
        return res

    def __repr__(self):
        """ print() or eval() __repr__ method function to return
            ... Rectangle(width, height)
        """
        w = str(self.__width)
        h = str(self.__height)

        res = "Rectangle(" + w + ", " + h + ")"
        return res

    def __del__(self):
        """ Print a message for del
        """
        print("Bye rectangle...")

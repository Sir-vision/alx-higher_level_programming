#!/usr/bin/python3
"""Defines a class class MagicClass"""

import math


class MagicClass:
    """Creates a new circle"""
    def __init__(self, radius=0):
        """Initializes the circle"""
        if (type(radius) != int) or (type(radius) != float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return (2 * math.pi) * self.__radius

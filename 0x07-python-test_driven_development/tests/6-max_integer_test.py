#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test different test cases"""
    def test_end(self):
        """Test for max if at the end"""
        sample = [1, 3, 0, 5]
        self.assertEqual(max_integer(sample), 5)

    def test_begining(self):
        """Test for max if at the begining"""
        sample = [5, 3, 0, 1]
        self.assertEqual(max_integer(sample), 5)

    def test_middle(self):
        """Test for max if at the middle"""
        sample = [1, 3, 7, 0, 5]
        self.assertEqual(max_integer(sample), 7)

    def test_negative(self):
        """Test for max any negative value exist"""
        sample = [1, 3, 0, -5]
        self.assertEqual(max_integer(sample), 3)

    def test_all_negative(self):
        """Test for max if all values are negative"""
        sample = [-1, -3, -7, -5]
        self.assertEqual(max_integer(sample), -1)

    def test_one_element(self):
        """Test for max if one element exist"""
        sample = [1]
        self.assertEqual(max_integer(sample), 1)

    def test_empty(self):
        """Test for max if its empty"""
        sample = []
        self.assertEqual(max_integer(sample), None)

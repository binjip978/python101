"""
simple functions
To run test:
    python3 function.py
To get a shell:
    python3 -i function.py
"""

import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    pass


def multiply(a, b):
    pass


def divide(a, b):
    pass


class TestArithmetic(unittest.TestCase):
    """
    Here we define test for add, subtract, multiply and divide functions
    To run suite:
        python3 functions.py TestArithmetic
    """

    def test_add(self):
        self.assertEqual(add(10, 20), 10 + 20)

    def test_subtract(self):
        self.assertEqual(subtract(10, 20), -10)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)


def increment(n):
    """takes n return n + 1"""
    return n + 1


class TestIncrement(unittest.TestCase):
    """
    Here we define tests for increment function
    To run suite:
        python3 functions.py TestArithmetic
    """

    def test_one(self):
        self.assertEqual(increment(10), 11)

    def test_fix_me(self):
        self.assertEqual(increment(20), 22)

    def test_fix_me_str(self):
        self.assertEqual(increment('41'), 42)

    def test_fix_function_arity(self):
        self.assertEqual(increment(10, 11))


def square(n):
    """return n times n"""
    pass


def cube(n):
    """return n ^ 3"""
    pass


def circumference(r):
    """return the distance around a circle"""
    pass


class TestShapes(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)

    def test_cube(self):
        self.assertEqual(cube(3), 27)
        self.assertEqual(cube(2), 8)

    def test_circumference(self):
        self.assertEqual(circumference(0), 0)

        res = circumference(1)
        self.assertTrue(abs(res - 6.283185307179586) < 0.00001)


if __name__ == '__main__':
    unittest.main()

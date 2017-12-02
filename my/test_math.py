import unittest
import my.math

class TestMy(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my.math.add(2, 3), 5)

    def test_sum(self):
        self.assertEqual(my.math.sum(2, 3, 4), 9)


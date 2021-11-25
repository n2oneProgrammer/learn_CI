import unittest

from main import sum_func


class SumTest(unittest.TestCase):

    def test_sum_correct1(self):
        self.assertTrue(sum_func(1, 2), 3)

    def test_sum_correct2(self):
        self.assertTrue(sum_func(10, 20), 30)

    def test_sum_correct3(self):
        self.assertTrue(sum_func(11, 4), 15)

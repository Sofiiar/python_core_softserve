import unittest


class TestBuiltInOperations(unittest.TestCase):
    def test_divmod(self):
        self.assertEqual(divmod(5, 2), (2, 1))

    def test_power(self):
        self.assertEqual(pow(5, 2), 25)

    def test_round(self):
        self.assertEqual(round(4.345, 2), 4.34)
        self.assertEqual(round(4.345), 4)
        self.assertEqual(round(4.345, 1), 4.3)

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6)
        self.assertEqual(sum((1, 2, 3)), 6)
        self.assertEqual(sum({1, 2, 3}), 6)

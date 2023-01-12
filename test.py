import unittest
from unittest import TestCase
import random
from calc import add, subtract, divide, multiply


class TestOperations(TestCase):
    def test_is_sum(self):
        a = random.randint(1, 100_000)
        b = random.randint(1, 100_000)
        print(self.assertEqual(add(a, b), a-b))


test = TestOperations()
test.test_is_sum()

import unittest
from unittest import TestCase
import random
from calc import add, subtract, divide, multiply


class TestOperations(TestCase):
    def test_is_sum(self):
        a = random.randint(1, 100_000)
        b = random.randint(1, 100_000)
        self.assertEqual(add(a, b), a+b)

    def test_is_difference(self):
        a = random.randint(1, 100_000)
        b = random.randint(1, 100_000)
        self.assertEqual(subtract(a, b), a-b)

    def test_is_product(self):
        a = random.randint(1, 100_000)
        b = random.randint(1, 100_000)
        self.assertEqual(multiply(a, b), a*b)

    def test_is_quotient(self):
        a = random.randint(1, 100_000)
        b = random.randint(1, 100_000)
        self.assertEqual(divide(a, b), a / b)


test = TestOperations()
test.test_is_sum()
test.test_is_difference()
test.test_is_product()
test.test_is_quotient()

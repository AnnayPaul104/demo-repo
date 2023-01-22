import time
from unittest import TestCase
import random
from calc import add, subtract, divide, multiply, square


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

    def test_is_square(self):
        a = random.randint(1, 100_000)
        self.assertEqual(square(a), a * a)

    def test_all(self):
        self.test_is_difference()
        self.test_is_product()
        self.test_is_quotient()
        self.test_is_sum()
        self.test_is_square()

    def test_exhaustive(self):
        start = time.time()
        for i in range(10000):
            self.test_all()
        print(f'Execution Time: {round(time.time()-start, 3)} seconds')


test = TestOperations()
test.test_exhaustive()

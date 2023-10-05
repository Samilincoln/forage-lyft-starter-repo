import unittest
from tire.octoprime import Octoprime

class testOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tirewear_values = [0.7, 0.7, 0.9, 0.1]
        wear_check = Octoprime(tirewear_values)
        self.assertTrue(wear_check.needs_service())

    def test_needs_service_false(self):
        tirewear_values = [0.1, 0.5, 0.1, 0.1]
        wear_check = Octoprime(tirewear_values)
        self.assertFalse(wear_check.needs_service())


if __name__ == '__main__':
    unittest.main()
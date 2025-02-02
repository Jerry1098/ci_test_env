import unittest
from src.prime import get_first_100_primes

class TestPrime(unittest.TestCase):
    def test_get_first_100_primes(self):
        result = get_first_100_primes()
        self.assertEqual(len(result), 100, "Should contain exactly 100 primes")
        for prime in result:
            self.assertTrue(prime > 1 and all(prime % k != 0 for k in range(2, int(prime ** 0.5) + 1)), "All numbers must be prime")

if __name__ == "__main__":
    unittest.main()

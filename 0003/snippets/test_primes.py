import unittest
import eratho
import prog


PRIMES = eratho.sieve(10 ** 6)


class TestPrimes(unittest.TestCase):
    def test_next_primes(self):
        assert prog.next_prime(2) == 2
        assert prog.next_prime(3) == 3
        assert prog.next_prime(5) == 5
        assert prog.next_prime(7) == 7
        assert prog.next_prime(9) == 11
        assert prog.next_prime(17) == 17
        assert prog.next_prime(18) == 19

    def test_is_prime(self):
        for n in [4, 6, 8, 9, 10, 12, 14, 16, 18]:
            assert not prog.is_prime(n), n

        for p in PRIMES:
            assert prog.is_prime(p), p

    def test_solution(self):
        assert prog.max_prime_factor(600851475143) == 6857

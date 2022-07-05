#!/usr/bin/env python

import sys
import math


def is_prime(n):
    assert n >= 2
    if n == 2:
        return True

    top = math.ceil(n ** (1/2))
    for i in range(2, top + 1):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    for i in range(n, 2 * n):
        if is_prime(i):
            return i
    raise Exception("No prime.")


def max_prime_factor(n):
    prime = 2
    max_prime = 0

    while n > 1:
        if n % prime == 0:
            n = n / prime
        else:
            prime = next_prime(prime + 1)

        if prime > max_prime:
            max_prime = prime
    return max_prime


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 600851475143
    print(max_prime_factor(n))

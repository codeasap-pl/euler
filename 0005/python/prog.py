#!/usr/bin/env python

# Inspired by:
# http://code.jasonbhill.com/python/project-euler-problem-5/

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    f = 3
    while n != 1:
        while n % f == 0:
            factors.append(f)
            n /= f
        f += 2
    return factors


def merge_factors(factors, new_factors, number):
    if not factors:
        factors.extend(new_factors)
        return

    uniq = set(new_factors)
    for f in uniq:
        if (new_factors.count(f) - factors.count(f)) > 0:
            factors.append(f)


def solution(n):
    factors = []
    for i in range(1, n + 1):
        merge_factors(factors, factorize(i), i)
    product = 1
    for f in factors:
        product *= f
    return product


if __name__ == "__main__":
    import sys
    import time

    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20

    start = time.perf_counter()
    product = solution(n)
    elapsed = (time.perf_counter() - start)
    print("{}, {:.12f}".format(product, elapsed))

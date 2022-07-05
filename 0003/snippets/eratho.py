import math


def sieve(n: int):
    """Seive of Erathostenes"""
    assert n > 1
    limit = n ** (1/2)  # sqrt
    limit = math.ceil(limit)

    A = [1] * n
    for i in range(2, limit):
        if A[i]:
            for j in range(i * 2, n, i):
                A[j] = 0

    return [idx for idx, val in enumerate(A) if val and idx >= 2]


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
    sieve(n)

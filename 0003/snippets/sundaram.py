def sieve(n: int):
    k = (n - 2) // 2
    A = [1] * (k + 1)
    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            A[i + j + 2 * i * j] = 0
            j += 1

    primes = [2 * i + 1 for i in range(1, k + 1) if A[i]]
    return ([2] if n > 2 else []) + primes


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
    sieve(n)

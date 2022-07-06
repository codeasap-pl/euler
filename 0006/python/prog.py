#!/usr/bin/env python


def simple(n):
    sq = 0
    s = 0
    for i in range(1, n + 1):
        s += i
        sq += i * i

    return s * s - sq


def lispy(n):
    s, sq = map(sum, zip(*[(_, _ * _) for _ in range(1, n + 1)]))
    return s * s - sq


def perl_golf(n):
    return [
        (k * k - v) for k, v in [
            list(map(sum, zip(*[(_, _ * _) for _ in range(1, n + 1)])))
        ]
    ][0]


if __name__ == "__main__":
    import lavka

    funcs = [simple, lispy, perl_golf]
    b = lavka.Benchmark()
    for f in funcs:
        grp = b.add_group(f.__qualname__)
        [
            grp.add_case(f, (n,), identifier="%s-%d" % (f.__qualname__, n))
            for n in [10 ** x for x in range(3, 7)]
        ]

    parser = b.create_parser()
    args = parser.parse_args()
    b(args)

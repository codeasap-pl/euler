import eratho
import sundaram

import lavka


variants = [eratho.sieve, sundaram.sieve]
limits = [10 ** i for i in range(4, 8)]

b = lavka.Benchmark()
for func in variants:
    grp = b.add_group(func.__module__)
    for n in limits:
        grp.add_case(
            func, args=(n, ),
            identifier="%s-%d" % (func.__module__, n)
        )

parser = b.create_parser()
b(parser.parse_args())

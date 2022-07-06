#include "std.h"

#ifdef SLOW
#include "slow/slow.h"
#endif

#ifdef FAST
#include "fast/fast.h"
#endif


void check_solution(unsigned long n, unsigned long smallest)
{
	unsigned long divisor;
	for(divisor = 2; divisor <= n; divisor++) {
		assert(smallest % divisor == 0);
	}
}

int main(int argc, char** argv)
{
	unsigned int n = (argc > 1 ? strtoul(argv[1], 0, 10) :  20);

	assert(n <= UINT_MAX);

	struct timespec t0, t1;
	clock_gettime(CLOCK_MONOTONIC_RAW, &t0);

#ifdef SLOW
	unsigned long long smallest = solution_slow_generic(n);
#endif

#ifdef FAST
	unsigned long long smallest = solution_fast(n);
#endif

	clock_gettime(CLOCK_MONOTONIC_RAW, &t1);

	check_solution(n, smallest);

	double dt = t1.tv_sec - t0.tv_sec;
	dt += (double) (t1.tv_nsec - t0.tv_nsec) / 1000 / 1000 / 1000;

	printf("%lld, %.16f\n", smallest, dt);
	return 0;
}

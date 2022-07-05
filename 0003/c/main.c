#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <assert.h>


int is_prime(int n)
{   /* naive */

	if(n < 2) { return 0; }
	else if(n == 2) { return 1; }

	int top = ceil(sqrt(n)) + 1;
	for(int i = 2; i < top; i++) {
		if(n % i == 0)
			return 0;
	}

	return 1;
}


int next_prime(int n)
{   /* naive prime gen. */

	for(int i = n; i < (2 * n); i++) {
		if(is_prime(i)) {
			return i;
		}
	}

	printf("NO PRIME! %d\n", n);
	assert(0);
}


void test()
{
	assert(next_prime(2) == 2);
	assert(next_prime(3) == 3);
	assert(next_prime(5) == 5);
	assert(next_prime(7) == 7);
	assert(next_prime(9) == 11);
	assert(next_prime(17) == 17);
	assert(next_prime(18) == 19);
}


int main(int argc, char *argv[])
{
	test();

	unsigned long number = (argc > 1 ? strtoul(argv[1], 0, 10) :  600851475143);

	int prime = 2;
	int max_prime = 0;

	while(number > 1) {
		if(number % prime == 0) {
			number /= prime;
		}
		else {
			prime = next_prime(prime + 1);
		}

		if(prime > max_prime) {
			max_prime = prime;
		}
	}

	printf("Max prime: %d\n", max_prime);

	return 0;
}

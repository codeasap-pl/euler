#include "slow.h"
#include "std.h"


unsigned long long solution_slow(unsigned int unused)
{
	unsigned long long found = 0;
	unsigned int i = 2520;

	while(!found && i < UINT_MAX) {
		if(i % 20 == 0 && /* 10, 5, 4, 2 */
		   i % 19 == 0 &&
		   i % 18 == 0 && /* 9, 6, 3 */
		   i % 17 == 0 &&
		   i % 16 == 0 && /* 8, 4 */
		   i % 15 == 0 && /* 5, 3 */
		   i % 14 == 0 && /* 7, 2 */
		   i % 13 == 0 &&
		   i % 12 == 0 && /* 6, 4, 3, 2 */
		   i % 11 == 0)
		{
			found = i;
			return found;
		}

		i++;
	}

	return found;
}


unsigned long long solution_slow_generic(unsigned int n)
{
	unsigned long long found = 0;
	unsigned int i = 0;

	while(!found && i < UINT_MAX) {
		found = i;
		for(unsigned int f = 2; f <= n; f++) {
			if(i % f != 0) {
				found = 0;
				break;
			}
		}

		i++;
	}

	return found;
}

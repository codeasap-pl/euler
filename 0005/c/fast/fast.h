#pragma once

#include "vector/vector.h"


void factorize(int n, struct vector_t *factors);
void merge_factors(struct vector_t *all_factors, const struct vector_t *new_factors);
unsigned long long solution_fast(unsigned int n);

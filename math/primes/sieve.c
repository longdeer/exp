

int* sieveArray(int size)
{
	int* sieve = calloc(size +1,sizeof(int));
	long long j;
	long long i;

	for(i = 2; i <= size; ++i) *(sieve +i) = 1;
	for(i = 2; i <= size; ++i)

		if(*(sieve +i))
			for(j = i*i; j <= size; j += i)
				*(sieve +j) = 0;

	return	sieve;
}


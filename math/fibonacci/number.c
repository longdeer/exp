

// dymaic programming array
int fib(int n)
{
	int* dp = malloc(sizeof(int) *(n +1));

	*dp = 0;

	for(int i = 1; i <= n; ++i) *(dp +i) = i == 1 ? 1 : *(dp +i -1) + *(dp +i -2);

	int number = *(dp +n);
	free(dp);
	dp = NULL;

	return number;
}


// recursion
int fib(int n)
{
	return !n ? 0 : n == 1 ? 1 : fib(n -1) + fib(n -2);
}


// iterative
int fib(int n)
{
	if(!n) return 0;

	int a = 0;
	int b = 1;
	int c;

	for(int i = 1; i <n; ++i)
	{
		c = a +b;
		a = b;
		b = c;
	}
	return b;
}


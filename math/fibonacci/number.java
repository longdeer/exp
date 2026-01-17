

// dymaic programming array
public int fib(int n) {

	int[] dp = new int[n+2]; Arrays.fill(dp,0); dp[1] = 1;
	for(int i = 2; i <= n; ++i) dp[i] = dp[i-1] + dp[i-2];
	return dp[n];
}


// recursion
public int fib(int n) {
	return n == 0 ? 0 : n == 1 ? 1 : fib(n-1) + fib(n-2);
}


// iterative
public int fib(int n) {

	if(n == 0) return 0;

	int a = 0;
	int b = 1;
	int c;

	for(int i = 1; i <n; ++i) {

		c = a +b;
		a = b;
		b = c;
	}
	return b;
}


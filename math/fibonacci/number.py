

# dymaic programming array
def fib(n: int) -> int:

	dp = [ 0,1 ]
	for _ in range(n -1): dp.append(dp[-1] + dp[-2])
	return dp[n]


# recursion
def fib(n: int) -> int:
	return 0 if n == 0 else 1 if n == 1 else fib(n -1) + fib(n -2)


# iterative
def fib(n: int) -> int:

	a,b = 0,1
	for _ in range(n -1): a,b = b,b+a
	return b if n else a


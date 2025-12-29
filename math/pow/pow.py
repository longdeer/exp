

# LeetCode Q50. Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


def myPow(x: float, n: int) -> float:

	r = s = 1
	if n <0 : s,n = -1,-1 *n

	while	0 <n:
		if	n &1: r *= x

		x *= x
		n >>= 1

	return	1 /r if s == -1 else r


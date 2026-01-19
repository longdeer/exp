

// LeetCode Q50. Pow(x, n)
// Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


public double myPow(double x, int n) {

	double r = 1;
	if(n <0) {

		n = -n;
		x = 1 /x;
	}
	while(n != 0) {
		if((n &1) != 0) {
			r *= x;
		}
		x *= x;
		n >>>= 1;
	}
	return r;
}


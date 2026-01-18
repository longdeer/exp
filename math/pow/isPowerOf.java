

// Leetcode Q231. Power of Two
// Given an integer n, return true if it is a power of two. Otherwise, return false.
// An integer n is a power of two, if there exists an integer x such that n == 2x.


public boolean isPowerOfTwo(int n) {
	return 0 <n && (-n &n) == n;
}


// Leetcode Q326. Power of Three
// Given an integer n, return true if it is a power of three. Otherwise, return false.
// An integer n is a power of three, if there exists an integer x such that n == 3x.


public boolean isPowerOfThree(int n) {
	return (Math.log(n) /Math.log(3) + 1e-10) %1 <= 1e-10 *2;
}


// Leetcode Q342. Power of Four
// Given an integer n, return true if it is a power of four. Otherwise, return false.
// An integer n is a power of four, if there exists an integer x such that n == 4x.


public boolean isPowerOfFour(int n) {
	return n > 0 && (n & (n - 1)) == 0 && (n & 0x55555555) != 0;
}


// General


public boolean isPowerOf(int n, int power) {

	while(0 <n && n %power == 0) n /= power;
	return n == 1;
}


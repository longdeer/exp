

// Leetcode Q231. Power of Two
// Given an integer n, return true if it is a power of two. Otherwise, return false.
// An integer n is a power of two, if there exists an integer x such that n == 2x.


bool isPowerOfTwo(int n)
{
	return 0 <n && (-n &n) == n;
}


// Leetcode Q326. Power of Three
// Given an integer n, return true if it is a power of three. Otherwise, return false.
// An integer n is a power of three, if there exists an integer x such that n == 3x.


bool isPowerOfThree(int n)
{
	return 0 <n && !(1162261467 %n);
}


// Leetcode Q342. Power of Four
// Given an integer n, return true if it is a power of four. Otherwise, return false.
// An integer n is a power of four, if there exists an integer x such that n == 4x.


bool isPowerOfFour(int n)
{
	return !!n && (-(long)n & n) == n && (1431655765 |n) == 1431655765;
}


// General


bool isPowerOf(int number, int power)
{
	while(0 <number && !(number %power)) number /= power;
	return number == 1;
}


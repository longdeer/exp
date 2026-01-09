

# Leetcode Q231. Power of Two
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.


def isPowerOfTwo(n: int) -> bool : return 0 <n and n.bit_count() == 1


# Leetcode Q326. Power of Three
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.


def isPowerOfThree(n: int) -> bool:

	if n <0 : return False
	if n == 1 : return True

	N = 1
	p = 3 **N

	while	p <= n:
		if	p == n : return True

		N += 1
		p = 3 **N

	return	False


# Leetcode Q342. Power of Four
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.


def isPowerOfFour(n: int) -> bool : return bool(n) and -n &n == n and 1431655765 |n == 1431655765


# General


def is_power_of(number :int, power :int) -> bool :

	while 0 <number and not number %power : number //= power
	return number == 1


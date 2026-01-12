

// Leetcode Q231. Power of Two
// Given an integer n, return true if it is a power of two. Otherwise, return false.
// An integer n is a power of two, if there exists an integer x such that n == 2x.


var isPowerOfTwo = n => 0 <n && !((n -1) &n);


// Leetcode Q326. Power of Three
// Given an integer n, return true if it is a power of three. Otherwise, return false.
// An integer n is a power of three, if there exists an integer x such that n == 3x.


var isPowerOfThree = n => n.toString(3).match(/^10*$/) !== null;


// Leetcode Q342. Power of Four
// Given an integer n, return true if it is a power of four. Otherwise, return false.
// An integer n is a power of four, if there exists an integer x such that n == 4x.


var isPowerOfFour = n => n.toString(4).match(/^10*$/) !== null;


// General


var powOf = (number, power) => {

	while(0 <number && !(number %power)) number = Math.floor(number /power);
	return number == 1
}




// Leetcode Q190. Reverse Bits
// Reverse bits of a given 32 bits signed integer.
// 0 <= n <= 231 - 2
// n is even.


int reverseBits(int n)
{
	int res = 0;
	for(int i = 0; i <32; ++i) res ^= n& (1l <<i) ? 1l <<(31 -i) : 0;
	return res;
}


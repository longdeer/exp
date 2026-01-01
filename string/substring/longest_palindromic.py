

# LeetCode Q5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.


def expander(text :str, left_index :int, right_index :int) -> int :

	L,R = left_index,right_index
	while	0 <= l and R <len(text) and text[L] == text[R] : L,R = L -1,R +1
	return	R -L -1

def longestPalindrome(s: str) -> str:

	distance = 0,0
	for i in range(len(s)):

		if	(reduce(lambda x,y : y -x, distance) +1) <(odds := expander(s, i,i)):

			current = odds //2
			distance = i- current,i+ current
		
		if	(reduce(lambda x,y : y -x, distance) +1) <(evens := expander(s, i,i +1)):

			current = (evens //2) -1
			distance = i- current,i+ current +1

	return	s[distance[0]:distance[1]+1]


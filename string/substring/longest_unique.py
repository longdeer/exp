

# LeetCode Q3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

def longest_unique_substring(s: str) -> int:

	if  s:
		L,U,longest,window = 0,1,1,str()

		while U <len(s):
			window = s[L:U]

			if	s[U] in window:

				longest,I = max(longest, len(window)),L
				while s[U] in s[I:U]:

					I += 1
				L = I
			U += 1

		return	max(longest, len(s[L:U]))
	return		0


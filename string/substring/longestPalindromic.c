

// LeetCode Q5. Longest Palindromic Substring
// Given a string s, return the longest palindromic substring in s.


int expand(char* s, int i, int j)
{
	while(-1 <i && j <strlen(s) && *(s +i) == *(s +j))
	{
		--i;
		++j;
	}
	return j -i -1;
}
char* longestPalindrome(char* s)
{
	int l = 0;
	int r = 0;
	int e;
	int c;
	int d;
	int i;

	for(i = 0; i <strlen(s); ++i)
	{
		d = r -l;
		e = expand(s, i,i);

		if(d <e)
		{
			c = e /2;
			l = i -c;
			r = i +c;
		}
		d = r -l;
		e = expand(s, i,i +1);

		if(d <e)
		{
			c = e /2 -1;
			l = i -c;
			r = i +c +1;
		}
	}
	char* palindrome = malloc(sizeof(char) *(r +2 -l));
	for(i = 0; i <r +1 -l; ++i) *(palindrome +i) = *(s +l +i);
	*(palindrome +i) = '\0';
	return palindrome;
}


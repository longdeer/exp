

// LeetCode Q3. Longest Substring Without Repeating Characters
// Given a string s, find the length of the longest substring without duplicate characters.

char* substring(char* src, int start, int end)
{
	int i = 0;
	char* sub = malloc(sizeof(char) *(end -start +1));
	while(start <end) *(sub +i++) = *(src+ start++);
	*(sub +i++) = '\0';
	return sub;
}
bool includes(char* src, char target)
{
	int i = 0;
	while(*(src +i))
	{
		if(*(src +i) == target) return true;
		++i;
	}
	return  false;
}
int max(int A, int B)
{
	return A <B ? B : A;
}
int lengthOfLongestSubstring(char* s)
{
	if(*s)
	{
		int i;
		int L = 0;
		int U = 1;
		int longest = 1;
		int j = strlen(s);
		char* window;

		while(U <j)
		{
			window = substring(s, L, U);

			if(includes(window, *(s +U)))
			{
				longest = max(longest, strlen(window));
				i = L;

				while(includes(substring(s, i, U), *(s +U))) ++i;
				L = i;
			}
			++U;
		}
		return	max(longest, strlen(substring(s, L, U)));
	}
	return	0;
}


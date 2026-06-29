

// LeetCode Q1967


int includes(char* container, char *target)
{
	int L = strlen(target);
	int i;
	int j;
	int t;

	for(i = 0; *(container +i); ++i)
	{
		j = 0;
		t = i;

		while(*(target +j))
			if(*(target +j) == *(container +i))
			{
				++i;
				++j;
			}
			else break;

		if(j == L) return 1;
		i = t;
	}
	return 0;
}


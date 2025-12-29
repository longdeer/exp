

// LeetCode Q10. Regular Expression Matching
// Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
//  '.' Matches any single character.
//  '*' Matches zero or more of the preceding element.
//  The matching should cover the entire input string (not partial).


bool helper(int** mem, int fms, int fmp, char*s, int sl, char* p, int pl)
{
	if(*(*(mem +fms) +fmp) == -1)
	{
		if(!(pl -fmp)) *(*(mem +fms) +fmp) = !(sl -fms); else
		if((fmp +1) <pl && *(p +fmp +1) == '*')

			*(*(mem +fms) +fmp) = (

				helper(mem, fms, fmp +2, s, sl, p, pl) ||
				(fms <sl && (*(p +fmp) == *(s +fms) || *(p +fmp) == '.')) &&
				helper(mem, fms +1, fmp, s, sl, p, pl)

			);	else

			*(*(mem +fms) +fmp) = (

				(fms <sl && (*(p +fmp) == *(s +fms) || *(p +fmp) == '.')) &&
				helper(mem, fms +1, fmp +1, s, sl, p, pl)
			);
	}
	return	*(*(mem +fms) +fmp);
}
bool isMatch(char* s, char* p) {

	int   i;
	int   j;
	int   sl = strlen(s);
	int   pl = strlen(p);
	int** dyna = malloc(sizeof(int*) *(sl +1));

	for(i = 0; i <= sl; ++i)
	{
		*(dyna +i) = malloc(sizeof(int) *(pl +1));
		for(j = 0; j <= pl; ++j) *(*(dyna +i) +j) = -1;
	}
	j = helper(dyna, 0, 0, s, sl, p, pl);

	for(i = 0; i <= sl; ++i)
	{
		free(*(dyna +i));
		*(dyna +i) = NULL;
	}
	free(dyna);
	dyna = NULL;

	return	j;
}


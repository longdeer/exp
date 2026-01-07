

// Leetcode Q224. Basic Calculator
// Given a string s representing a valid expression, implement a basic calculator to evaluate it,
// and return the result of the evaluation.
// Note: You are not allowed to use any built-in function which evaluates strings
// as mathematical expressions, such as eval().


int dump(char* c, int i)
{
	if(!i) return 0;

	long k = 0;
	int  s = 1;
	int  j = 0;

	if(*c == '-')
	{
		s = -1;
		j = 1;

	}
	while(j <i)
	{
		k *= 10;
		k += *(c +j++) - '0';
	}
	return (int)(k *s);
}
int calculate(char* s)
{
	int L = strlen(s);
	int i = 0;
	int j = 0;
	int k = 0;
	int l = 0;

	int*  result = calloc((L +1), sizeof(int));
	int*  signs = malloc(sizeof(char) *(L +1));
	char* current = malloc(sizeof(char) *(L +1));

	while(*(s +l))
	{
		switch(*(s +l))
		{
			case '-':

				*(result +i) += dump(current,k);
				*current = '-';
				k = 1;
				++l;
				break;

			case '+':

				*(result +i) += dump(current,k);
				k = 0;
				++l;
				break;

			case '(':

				++i;
				*(signs +j++) = k ? -1 : 1;
				k = 0;
				++l;
				break;

			case ')':

				*(result +i) += dump(current,k);
				*(result +i -1) += *(result +i)* *(signs +j-- -1);
				*(result +i--) = 0;
				k = 0;
				++l;
				break;

			case ' ':

				++l;
				break;

			default:

				*(current +k++) = *(s +l++);
				break;
		}
	}
	return	*(result +i) + dump(current,k);
}


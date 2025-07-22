

char* uintConvert(uint n, int radix, bool capital)
{
	char* base = malloc(sizeof(char) *33);
	char* converted;
	int   i = 0;
	int   j = 0;
	int   rem;

	while(n)
	{
		rem = n %radix;
		*(base +i++) = (char)(rem + (rem <10 ? '0' : (capital ? 'A' : 'a') -10));
		n /= radix;
	}
	converted = malloc(sizeof(char) *(i-- +1));
	while(-1 <i) *(converted +j++) = *(base +i--);
	*(converted +j) = '\0';

	free(base);
	base = NULL;

	return converted;
}


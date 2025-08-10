

// LC3479
void build(int node, int l, int r, int* st, int* src)
{
	if(l == r) *(st + node) = *(src +l);
	else
	{
		int m = l + (r -l) /2;
		int f = node <<1;

		build(f, l,m, st,src);
		build(f +1, m +1,r, st,src);

		*(st + node) = *(st +f) <*(st +f +1) ? *(st +f +1) : *(st +f);
	}
}
int update(int node, int l, int r, int* st, int T)
{
	if(l == r)
	{
		if(T <= *(st + node))
		{
			*(st + node) = 0;
			return 1;
		}	return 0;
	}
	int m = l + (r -l) /2;
	int f = node <<1;

	if(T <= *(st + f) && update(f, l,m, st, T))
	{
		*(st + node) = *(st +f) <*(st +f +1) ? *(st +f +1) : *(st +f);
		return 1;
	}
	if(T <= *(st +f +1) && update(f +1, m +1,r, st, T))
	{
		*(st + node) = *(st +f) <*(st +f +1) ? *(st +f +1) : *(st +f);
		return 1;
	}	return 0;
}


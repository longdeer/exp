def power(self, b :int, e :int) -> int :

	r = 1

	while	0 <e:
		if	e &1 : r = (r*b) %1000000007

		b = (b*b) %1000000007
		e >>= 1

	return r
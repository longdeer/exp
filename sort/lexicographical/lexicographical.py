from itertools	import zip_longest








def lexicographical(A :int, B :int) -> int :

	for a,b in zip_longest(str(A), str(B), fillvalue="0"):

		if	a <b : return -1
		if	b <a : return 1
	return	0








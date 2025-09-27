

def fraction_to_decimal(numerator: int, denominator: int) -> str:

	if not numerator %denominator : return str(numerator // denominator)

	N = abs(numerator)
	D = abs(denominator)
	sign = "" if (0 <numerator and 0 <denominator) or (numerator <0 and denominator <0) else "-"
	d = ""

	if	N <D:

		b = N *10
		r = "0"
	else:

		b = N // D
		r = str(b)
		b = (N- (b *D)) *10

	while b <D:

		b *= 10
		d += "0"

	ht = dict()
	i = len(d)

	while b:

		ht[b] = i
		i += 1
		x = b //D
		d += str(x)
		b = (b- (D *x)) *10

		while b and b <D:

			d += "0"
			b *= 10
		if	b in ht : return f"{sign}{r}.{d[:ht[b]]}({d[ht[b]:]})"
	return	f"{sign}{r}.{d}"


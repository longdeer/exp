

def convert(n :int, radix, capital=False) -> str :

		assert 1 <radix <37
		base = str()

		while(n):

			rem = n %radix
			base = (str(rem) if rem <10 else chr((55 if capital else 87) +rem)) + base
			n //= radix

		return base


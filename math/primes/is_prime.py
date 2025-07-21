

def is_prime(n :int) -> bool :

	if	n <2 : return False
	if	n in ( 2,3 ): return True
	if	not n%2 or not n%3 : return False

	for i in range(5,int(n **.5),6):
		if	not n%i or not n%(i+2): return False
	return	True


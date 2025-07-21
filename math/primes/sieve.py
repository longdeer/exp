

def sieve_list(size :int) -> List[int] :

	sieve = [ True ] *(size +1)

	for i in range(2,size +1):
		if	sieve[i]:

			for j in range(i*i,size +1,i):
				sieve[j] = False

	return	[ i for i,S in enumerate(sieve) if S ][2:]


def sieve_generator(size :int) -> Generator[int,None,None] :

	sieve = [ True ] *(size +1)

	for i in range(2,size +1):

		if	sieve[i]:
			yield i

			for j in range(i*i,size +1,i):
				sieve[j] = False


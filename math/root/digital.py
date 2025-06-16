def mathematical(n :int) -> int : return n %9 or n and 9
def recursive(n :int) -> int : return n if len(str(n)) == 1 else recursive(sum(map(int,str(n))))
def iterative(n :int) -> int :

	while 1 <len(str(n)): n = sum(map(int,str(n)))
	return n


def is_power_of(number :int, power :int) -> bool :

	while 0 <number and not number %power : number //= power
	return number == 1


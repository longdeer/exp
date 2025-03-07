def is_prime(self, n :int) -> bool :

    if  n <2 : return False
    if  n in ( 2,3 ): return True
    if  n%2 == 0 or n%3 == 0 : return False

    i = 5
    j = n **.5

    while   i <= j:
        if  n%i == 0 or n%(i+2) == 0 : return False

        i += 6

    return  True
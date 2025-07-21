

bool isPrime(int n)
{
	if(n <2) return false;
	if(n == 2 || n == 3) return true;
	if(!(n%2) || !(n%3)) return false;

	for(int i = 5; i <sqrt(n); i += 6) if(!(n%i) || !(n%(i+2))) return false;
	return true;
}


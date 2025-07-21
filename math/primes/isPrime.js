

var isPrime = function(n) {

	if(n <2) return false;
	if(n === 2 || n === 3) return true;
	if(n%2 === 0 || n%3 === 0) return false;

	for(var i = 5; i <n **.5; i += 6) if(n%i === 0 || n%(i+2) === 0) return false;
	return true
}


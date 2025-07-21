

var sieveArray = function(size) {

	var j;
	var sieve = Array.from(new Array(size +1),i => true);

	for(var i = 2; i <= size; ++i)

		if(sieve[i])
			for(j = i*i; j <= size; j += i)
				sieve[j] = false;

	return  sieve.map((s,i) => s ? i : null).filter(i => Boolean(i)).slice(1)
}

function* sieveGenerator(size) {

	var j;
	var sieve = Array.from(new Array(size +1),i => true);

	for(var i = 2; i <= size; ++i)

		if(sieve[i]) {
			yield i;

			for(j = i*i; j <= size; j += i)
				sieve[j] = false;
		}
}


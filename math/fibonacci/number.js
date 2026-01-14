

// dymaic programming array
var fib = function(n) {

	var dp = [ 0,1 ];
	while(dp[n] == null) dp[dp.length] = dp[dp.length-1] + dp[dp.length-2];
	return dp[n]
}

// recursion
var fib = function(n) {
	return n === 0 ? 0 : n === 1 ? 1 : fib(n-1) + fib(n-2)
}


// iterative
var fib = function(n) {

	if(n === 0) return 0;

	var a = 0;
	var b = 1;
	var m = 2;

	while(m++ <= n) [ a,b ] = [ b,b +a ];
	return b
}


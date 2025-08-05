

// LC2756
// Batching multiple small queries into a single large query can be a useful optimization.
// Write a class QueryBatcher that implements this functionality.
// The constructor should accept two parameters:
//		- An asynchronous function queryMultiple which accepts an array of string keys input.
//		It will resolve with an array of values that is the same length as the input array.
//		Each index corresponds to the value associated with input[i].
//		You can assume the promise will never reject.
//		- A throttle time in milliseconds t.
// The class has a single method.
//		- async getValue(key). Accepts a single string key and resolves with a single string value.
//		The keys passed to this function should eventually get passed to the queryMultiple function.
//		queryMultiple should never be called consecutively within t milliseconds.
//		The first time getValue is called, queryMultiple should immediately be called
//		with that single key. If after t milliseconds, getValue had been called again,
//		all the passed keys should be passed to queryMultiple and ultimately returned.
//		You can assume every key passed to this method is unique.


var QueryBatcher = function(queryMultiple, t) {

	this.fn = queryMultiple;
	this.t = t;
	this.pool = [];
	this.ready = true;
}
QueryBatcher.prototype.throttle = function() {

	setTimeout(() => {
		if(!this.pool.length) {

			this.ready = true;
			return
		}
		const keys = [];
		const resolvers = [];

		this.pool.forEach(([ R,K ]) => { keys.push(K); resolvers.push(R) });
		this.pool = [];

		this.fn(keys).then(values => resolvers.forEach((R,i) => R(values[i])));
		this.throttle()
	},	this.t)
}
QueryBatcher.prototype.getValue = function(key) {

	return new Promise(res => {
		if(this.ready) {

			this.ready = false;
			this.fn([ key ]).then(values => res(values[0]));
			this.throttle();
			return
		}	this.pool.push([ res,key ])
	})
}


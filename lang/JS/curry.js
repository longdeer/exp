

// LC2632


var curry1 = function(fn) {

	var current = new Array;
	var L = fn.length;
	
	return function curried() {

		if(current.length + arguments.length === L) return fn(...current,...arguments);
		current.push(...arguments);
		return (...next) => curried(...next)
	}
}


var curry2 = function(fn) {
	return function curried(...args) {

		if(args.length === fn.length) return fn.apply(this, args);
		return curried.bind(this, ...args)
	}
}


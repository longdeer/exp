

function memoize(fn) {

	const cach = new Map();
	let current;
	let size;
	let i;

	return function() {

		size = arguments.length;

		if(!cach.has(size)) cach.set(size,size ? new Map() : fn());

		current = cach.get(size);

		for(i = 0; i <arguments.length; ++i) {

			if(!current.has(arguments[i]))
				current.set(arguments[i],i === size -1 ? fn(...arguments) : new Map());

			current = current.get(arguments[i])
		}
		return current
	}
}


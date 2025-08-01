

// LC2777
// Given a start date start, an end date end, and a positive integer step,
// return a generator object that yields dates in the range from start to end inclusive.
// The value of step indicates the number of days between consecutive yielded values.
// All yielded dates must be in the string format YYYY-MM-DD


function* dateRangeGenerator(start, end, step) {

	let current = new Date(start);
	let finish = new Date(end);

	while(current <= finish) {

		yield current.toISOString().substring(0,10);
		current = new Date(current.getTime() + 864E5 *step)
	}
}


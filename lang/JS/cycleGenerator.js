

// LC2757
// Given a circular array arr and an integer startIndex,
// return a generator object gen that yields values from arr.
// The first time gen.next() is called on the generator, it should should yield arr[startIndex].
// Each subsequent time gen.next() is called, an integer jump will be passed into the function
// (Ex: gen.next(-3)).
//		If jump is positive, the index should increase by that value,
//		however if the current index is the last index, it should instead jump to the first index.
//		If jump is negative, the index should decrease by the magnitude of that value,
//		however if the current index is the first index, it should instead jump to the last index.


function* cycleGenerator1(arr, startIndex) {

	let newIndex = startIndex;
	let jump;

	while(true) {

		jump = yield arr[newIndex];
		newIndex = (newIndex + arr.length + jump %arr.length) %arr.length
	}
}


function* cycleGenerator2(arr, startIndex) {

	while(true) {

		jump = yield arr.at(startIndex %arr.length);
		startIndex += jump
	}
}


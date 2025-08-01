

// LC2628
// Given two values o1 and o2, return a boolean value indicating whether two values, o1 and o2, are deeply equal.
// For two values to be deeply equal, the following conditions must be met:
//		-If both values are primitive types, they are deeply equal if they pass the === equality check.
//		-If both values are arrays, they are deeply equal if they have the same elements in the same order,
//		and each element is also deeply equal according to these conditions.
//		-If both values are objects, they are deeply equal if they have the same keys,
//		and the associated values for each key are also deeply equal according to these conditions.
// You may assume both values are the output of JSON.parse. In other words, they are valid JSON.


function areDeeplyEqual(o1, o2) {

	if(Array.isArray(o1) && Array.isArray(o2)) {

		if(o1.length !== o2.length) return false;
		for(let i = 0; i <o1.length; ++i)
			if(!areDeeplyEqual(o1[i], o2[i])) return false;
		return true
	}
	if(o1 && !Array.isArray(o1) && typeof o1 === "object" && o2 && !Array.isArray(o2) && typeof o2 === "object") {

		let o1k = Object.keys(o1).sort();
		let o2k = Object.keys(o2).sort();

		if(o1k.length !== o2k.length) return false;
		for(let i = 0; i <o1k.length; ++i) {

			if(!areDeeplyEqual(o1k[i], o2k[i])) return false;
			if(!areDeeplyEqual(o1[o1k[i]], o2[o2k[i]])) return false;
		}
		return true
	}	return o1 === o2
}


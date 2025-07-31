

// LC2755
// Given two values A and B, return a deepmerged value.
// Values should be deepmerged according to these rules:
//		- If the two values are objects, the resulting object should have all the keys
//		that exist on either object. If a key belongs to both objects,
//		deepmerge the two associated values.
//		Otherwise, add the key-value pair to the resulting object.
//		- If the two values are arrays, the resulting array should
//		be the same length as the longer array.
//		Apply the same logic as you would with objects, but treat the indices as keys.
//		- Otherwise the resulting value is B.
// You can assume A and B are the output of JSON.parse().


var deepMerge = function(A, B) {

	if(A && typeof(A) === "object" && B && typeof(B) === "object" && Array.isArray(A) === Array.isArray(B)) {
		for(let key of new Set([ ...Object.keys(A),...Object.keys(B) ]))

			B[key] = deepMerge(A[key],B[key]);
	}
	return	B === undefined ? A : B
}


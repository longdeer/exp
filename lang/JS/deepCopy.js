

function deepCopy(A) {

	if(A && typeof(A) === "object") {

		let B = Array.isArray(A) ? [] : {};
		for(let key in A) B[key] = this.deepCopy(A[key]);

		return B
	}	return A
}


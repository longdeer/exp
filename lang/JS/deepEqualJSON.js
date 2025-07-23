

// LC2628
// Assumed "o1" and "o2" are the output of JSON.parse (valid JSON)


var areDeeplyEqual = function(o1, o2) {

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
	}
	return o1 === o2
}


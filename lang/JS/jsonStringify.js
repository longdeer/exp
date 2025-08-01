

// LC2633
// Given a value, return a valid JSON string of that value.
// The value can be a string, number, array, object, boolean, or null.
// The returned string should not include extra spaces.
// The order of keys should be the same as the order returned by Object.keys().


function jsonStringify(O) {

	if(Array.isArray(O)) return "[" + O.map(E => jsonStringify(E)).join() + "]";
	if(O && typeof O === "object")
		return "{" + Array.prototype.map.call(Object.keys(O),K => `${jsonStringify(K)}:${jsonStringify(O[K])}`).join() + "}"
	if(typeof(O) === "string") return `"${O}"`;
	return String(O)
}


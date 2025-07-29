

// LC2775
// Given a deeply nested object or array obj, return the object obj
// with any undefined values replaced by null.
// undefined values are handled differently than null values when objects are converted
// to a JSON string using JSON.stringify(). This function helps ensure serialized data
// is free of unexpected errors.


function undefinedToNull1(obj) {

	let stak = [ obj ];
	let current;

	while(0 <stak.length) {

		current = stak.pop();

		if(Array.isArray(current))
			for(let i = 0; i <current.length; ++i) {

				if(current[i] === undefined) current[i] = null;
				else
				if(current[i] && typeof(current[i]) === "object") stak.push(current[i])
			}	else

		if(current && typeof(current) === "object")
			for(key in current) {

				if(current[key] === undefined) current[key] = null;
				else
				if(current[key] && typeof(current[key]) === "object") stak.push(current[key])
			}
	}
	return obj
}


function undefinedToNull2(obj) {

	if(typeof(obj) !== "object" || obj === null) return obj === undefined ? null : obj;
	if(Array.isArray(obj)) return obj.map(E => undefinedToNull(E));

	const newObject = {}

	for(let key in obj) newObject[key] = undefinedToNull(obj[key]);
	return newObject
}


function undefinedToNull3(obj) {

	if(obj === undefined) return null;
	if(typeof(obj) === "object") {

		for(let key in obj) obj[key] = undefinedToNull(obj[key]);
		return obj
	}	return obj
}


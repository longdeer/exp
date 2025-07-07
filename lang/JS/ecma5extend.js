

function extend(o) {

	var i;
	var src;
	var prop;

	/*
		The first part is a standard behaviour for environments other than IE,
		which is known to have a certain bug for properties enumeration.
	*/
	for(var p in { toString: null })
		for(i = 1; i <arguments.length; ++i) {

			src = arguments[i];
			for(prop in src) o[prop] = src[prop]
		}
		return o;

	/*
		This point means it is IE environment, so the bug when for/in loop
		won't enumerate an enumerable property of "o" if the prototype of "o"
		has a nonenumerable property by the same name.
	*/
	for(i = 1; i <arguments.length; ++i) {

		src = arguments[i];

		for(prop in src) o[prop] = src[prop];
		for(var j = 0; j <neprops.length; ++j) {

			prop = neprops[j];
			if(src.hasOwnProperty(prop)) o[prop] = src[prop]
		}
	}
	var neprops = [

		"valueOf",
		"toString",
		"toLocalString",
		"constructor",
		"hasOwnProperty",
		"isPrototypeOf",
		"propertyIsEnumerable"
	];
	return o
}


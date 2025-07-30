

// LC2692
// Write a function that takes an object obj and returns a new immutable version of this object.
// An immutable object is an object that can't be altered and will throw an error
// if any attempt is made to alter it.
// There are three types of error messages that can be produced from this new object.
//		Attempting to modify a key on the object will result in this error message:
//			`Error Modifying: ${key}`.
//		Attempting to modify an index on an array will result in this error message:
//			`Error Modifying Index: ${index}`.
//		Attempting to call a method that mutates an array will result in this error message:
//			`Error Calling Method: ${methodName}`.
// You may assume the only methods that can mutate an array are
// ['pop', 'push', 'shift', 'unshift', 'splice', 'sort', 'reverse'].
// obj is a valid JSON object or array, meaning it is the output of JSON.parse()


function makeImmutable(obj) {

	const restrictedMethods = new Set([ "pop", "push", "shift", "unshift", "splice", "sort", "reverse" ]);
	const handler = {

		set(target, prop) {
			throw `Error Modifying${Array.isArray(target) ? " Index" : ""}: ${prop}`
		},
		get(target, prop) {
			return  prop === "prototype" ||
					target[prop] === null ||
					typeof(target[prop]) !== "object" &&
					typeof(target[prop]) !== "function" ?
					target[prop] : new Proxy(target[prop],this)
		},
		apply(target, ...rest) {

			if(restrictedMethods.has(target.name)) throw `Error Calling Method: ${target.name}`;
			return target.apply(...rest)
		}
	}
	return	new Proxy(obj,handler)
}


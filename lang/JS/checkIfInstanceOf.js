

// LC2618
// Write a function that checks if a given value is an instance of a given class or superclass.
// For this problem, an object is considered an instance of a given class
// if that object has access to that class's methods.
// There are no constraints on the data types that can be passed to the function.
// For example, the value or the class could be undefined.


var checkIfInstanceOf = function(obj, classFunction) {

	if(classFunction === undefined) return false;
	if(classFunction === null) return false;
	if(obj === undefined) return false;
	if(obj === null) return false;

	return	classFunction.prototype === Object.getPrototypeOf(obj) ? true :
			checkIfInstanceOf(Object.getPrototypeOf(obj), classFunction);
}


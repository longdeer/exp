

// LC2691
// Creating clones of immutable objects with minor alterations can be a tedious process.
// Write a class ImmutableHelper that serves as a tool to help with this requirement.
// The constructor accepts an immutable object obj which will be a JSON object or array.
// The class has a single method produce which accepts a function mutator.
// The function returns a new object which is similar to the original except it has those mutations applied.
// mutator accepts a proxied version of obj. A user of this function can (appear to) mutate this object,
// but the original object obj should not actually be effected.
// For example, a user could write code like this:
//		const originalObj = {"x": 5};
//		const helper = new ImmutableHelper(originalObj);
//		const newObj = helper.produce((proxy) => {
//		  proxy.x = proxy.x + 1;
//		});
//		console.log(originalObj); // {"x": 5}
//		console.log(newObj); // {"x": 6}
// Properties of the mutator function:
//		It will always return undefined.
//		It will never access keys that don't exist.
//		It will never delete keys (delete obj.key)
//		It will never call methods on a proxied object (push, shift, etc).
//		It will never set keys to objects (proxy.x = {})


var ImmutableHelper = function (obj) {
	this.inner = obj
}
ImmutableHelper.prototype.produce = function (mutator) {

	const mutated = { _: this.inner };
	mutator(proxify(mutated,{ _: this.inner },(field, value) => { mutated[field] = value; return mutated })._);

	return mutated._;

	function proxify(mutableObj, originalObj, setter) {
		return new Proxy(mutableObj,{

			set(_, prop, value) { mutableObj = setter(prop, value) },
			get(_, prop) {

				let value = mutableObj[prop];

				if(!value || typeof(value) !== "object") return value;
				else return proxify(value, originalObj[prop], (field, newValue) => {

					if(value === originalObj[prop])
						mutableObj = setter(prop, value = Array.isArray(value) ? [ ...value ] : { ...value });

					value[field] = newValue;
					return value
				})
			}
		})
	}
}


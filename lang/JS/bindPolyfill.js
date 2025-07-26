

// LC2754
// Enhance all functions to have the bindPolyfill method.
// When bindPolyfill is called with a passed object obj,
// that object becomes the this context for the function.
// For example, if you had the code:
//		function f() {
//		  console.log('My context is ' + this.ctx);
//		}
//		f();
// The output would be "My context is undefined". However, if you bound the function:
//		function f() {
//		  console.log('My context is ' + this.ctx);
//		}
//		const boundFunc = f.boundPolyfill({ "ctx": "My Object" })
//		boundFunc();
// The output should be "My context is My Object".
// You may assume that a single non-null object will be passed to the bindPolyfill method.


Function.prototype.bindPolyfill = function(obj) {

	let F = Symbol();
	obj[F] = this;
	return (...args) => obj[F](...args)
}


Function.prototype.bindPolyfill = function(obj) {
	return (...args) => this.call(obj,...args)
}


Function.prototype.bindPolyfill = function(obj) {
	return (...args) => this.apply(obj,args)
}


Function.prototype.bindPolyfill = function(obj) {
	return this.bind(obj)
}


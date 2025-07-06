

function inherit(o) {

	if(o == null) throw TypeError("Can't inherit from null objects");
	if(Object.create) return Object.create(o);

	var t = typeof o;
	if(t !== "object" && t !== "function") throw TypeError("Can inherit only valid Objects");

	function f(){};
	f.prototype = o;

	return new f()
}


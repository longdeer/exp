

Array.prototype.reduce = Array.prototype.reduce || function(f,initial) {

	var acc;
	var i = 0;
	var len = this.length;
	console.log("go");

	if(2 <arguments.length) acc = initial;
	else {

		if(!len) throw TypeError("Reducing empty Array");
		while(i <len) {
			if(i in this) {

				acc = this[i++];
				break
			}
			++i
		}
		if(i == len) throw TypeError("No elements to reduce")
	}
	while(i <len) {

		if(i in this) acc = f.call(undefined, acc, this[i], i, this);
		++i
	}
	return acc
}




Array.prototype.map = Array.prototype.map || function(f) {

	var results = [];
	for(var i = 0; i <this.length; ++i) if(i in this) results[i] = f.call(null, this[i], i, this);
	return results
}




function ElementStream(E) {

	if(typeof(E) === "string") E = document.getElementById(E);

	this.E = E;
	this.buffer = ""
}
ElementStream.prototype.write = function() {
	this.buffer += Array.prototype.join.call(arguments,"")
}
ElementStream.prototype.writeln() = function() {
	this.buffer += Array.prototype.join.call(arguments,"") + "\n"
}
ElementStream.prototype.close = function() {

	this.E.innerHTML = this.buffer;
	this.buffer = ""
}




/*
 *	JavaScript: The Definitive Guide
 *	16.5 Scripting CSS Classes
 *	Example 16-5. classList(): treat className as a set of CSS classes
 */

function classList(element) {

	if(element.classList) return element.classList;
	return new CSSClassList(element)
}
function CSSClassList(element) {
	this.element = element
}
CSSClassList.prototype.contains = function(target) {

	if(!target.length || target.indexOf(" ") != -1)
		throw new Error("Invalid class name: '" + target + "'");

	var classes = this.element.className;

	if(!classes) return false;
	if(classes === target) return true;

	return classes.search("\\b" + target + "\\b") != -1
}
CSSClassList.prototype.add = function(target) {

	if(this.contains(target)) return;

	var classes = this.element.className;

	if(classes && classes[classes.length-1] != " ") target = " " + target;

	this.element.className += target
}
CSSClassList.prototype.remove = function(target) {

	if(!target.length || target.indexOf(" ") != -1)
		throw new Error("Invalid class name: '" + target + "'");

	var pattern = new RegExp("\\b" + target + "\\b\\s*","g");
	this.element.className = this.element.className.replace(pattern,"")
}
CSSClassList.prototype.toggle = function(target) {

	if(this.contains(target)) {

		this.remove(target);
		return false

	}	else {

		this.add(target);
		return true
	}
}
CSSClassList.prototype.toString = function() {
	return this.element.className
}
CSSClassList.prototype.toArray = function() {
	return this.element.className.match(/\b\w+\b/g) || []
}




// Leetcode Q224. Basic Calculator
// Given a string s representing a valid expression, implement a basic calculator to evaluate it,
// and return the result of the evaluation.
// Note: You are not allowed to use any built-in function which evaluates strings
// as mathematical expressions, such as eval().


var calculate = function(s) {

	var signs = [];
	var result = [ 0 ];
	var current = "";
	var prev;

	for(var chr of s) {
		switch(chr) {

			case "-":

				result[result.length-1] += current.length ? parseInt(current) : 0;
				current = "-";
				break;

			case "+":

				result[result.length-1] += current.length ? parseInt(current) : 0;
				current = "";
				break;

			case "(":

				result.push(0);
				signs.push(current.length ? -1 : 1);
				current = "";
				break;

			case ")":

				result[result.length-1] += current.length ? parseInt(current) : 0;
				prev = result.pop() * signs.pop();
				result[result.length-1] += prev;
				current = "";
				break;

			case " ":

				continue;

			default:

				current += chr;
				break;
		}
	}	return	result[result.length-1] + (current.length ? parseInt(current) : 0);
}


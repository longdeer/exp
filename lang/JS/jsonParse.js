

// LC2759
// Given a string str, return parsed JSON parsedStr.
// You may assume the str is a valid JSON string hence it only includes
// strings, numbers, arrays, objects, booleans, and null.
// str will not include invisible characters and escape characters.


function jsonParse(str) {

	let current;
	let i = 0,j = -1;
	let keys = [],stack = [];
	let stops = new Set(",}]");

	while(i <str.length) {
		switch(str[i]) {

			case "{": stack.push({}); ++i; ++j; break;
			case "[": stack.push([]); ++i; ++j; break;
			case ",": ++i; break;
			case "}":
			case "]":

				++i; current = stack.pop(); --j;
				if(j === -1) return current;
				if(Array.isArray(stack[j])) stack[j].push(current);
				else stack[j][keys.pop()] = current;
				break;

			case "\"":

				++i; current = ""; while(str[i] !== "\"") current += str[i++]; ++i;
				if(j === -1) return current;
				if(Array.isArray(stack[j])) stack[j].push(current);
				else if(str[i] === ":") { keys.push(current); ++i }
				else stack[j][keys.pop()] = current;
				break;

			default:

				current = "";
				while(str[i] && !stops.has(str[i])) current += str[i++];
				switch(current) {

					case "true":  current = true;  break;
					case "false": current = false; break;
					case "null":  current = null;  break;
					default:      current = current.includes(".") ? parseFloat(current) : parseInt(current); break;
				}
				if(j === -1) return current;
				if(Array.isArray(stack[j])) stack[j].push(current);
				else stack[j][keys.pop()] = current;
				break;
		}
	}
}


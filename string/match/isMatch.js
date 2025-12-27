

// 10. Regular Expression Matching
// Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
//  '.' Matches any single character.
//  '*' Matches zero or more of the preceding element.
//  The matching should cover the entire input string (not partial).


var isMatch = function(s, p) {
	var dyna = new Map();

	function deep(fms, fmp) {
		var current = `${fms},${fmp}`;

		if(!dyna.has(current)) {

			if(!(p.length -fmp)) dyna.set(current,!(s.length -fms)); else
			if((fmp +1) <p.length && p[fmp+1] === "*")

				dyna.set(current,

					deep(fms, fmp +2) ||
					(fms <s.length && (p[fmp] === s[fms] || p[fmp] === ".")) &&
					deep(fms +1, fmp)
				);
			else
				dyna.set(current,

					(fms <s.length && (p[fmp] === s[fms] || p[fmp] === ".")) &&
					deep(fms +1, fmp +1)
				)
		}	return	dyna.get(current)
	}	return	deep(0,0)
}


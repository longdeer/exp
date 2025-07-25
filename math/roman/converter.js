

function romanToInt(s) {

	var prev = 0;
	var current;
	var n = 0;

	for(var chr of Array.prototype.toReversed.call(s)) {
		switch(chr) {

			case "I": current = 1; break;
			case "V": current = 5; break;
			case "X": current = 10; break;
			case "L": current = 50; break;
			case "C": current = 100; break;
			case "D": current = 500; break;
			case "M": current = 1000; break;
		}
		if(current <prev) n -= current;
		else n += current;
		prev = current
	}
	return n
}


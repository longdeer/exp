

function recursiveFastex(b,e) {

	if(!e) return 1;
	var r = recursiveFastex(b,e >>1)
	return (e &1 ? b*r*r : r*r);
}


function iterativeFastex(b,e) {

	var r = 1;

	for(; e; e >>= 1) {

		if(e &1) r = b*r;
		b = b*b;
	}
	return r;
}



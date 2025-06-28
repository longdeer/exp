function fastex(b,e) {

	var r = 1;

	for(; e; e >>= 1) {

		if(e &1) r = b*r %1000000007;
		b = b*b %1000000007;
	}
	return r;
}


var fractionToDecimal = function(numerator, denominator) {

	if(!(numerator % denominator)) return `${numerator / denominator}`;

	let b,r,x;
	let d = "";
	let N = Math.abs(numerator);
	let D = Math.abs(denominator);
	let sign = (0 <numerator && 0 <denominator) || (numerator <0 && denominator <0) ? "" : "-";

	if(N <D) {

		b = N *10;
		r = "0"

	}	else {

		b = Math.floor(N /D);
		r = `${b}`;
		b = (N- (b *D)) *10
	}
	while(b <D) {

		b *= 10;
		d += "0"
	}
	const ht = {};
	let   i = d.length;

	while(b) {

		ht[b] = i++;
		x = Math.floor(b /D);
		d = `${d}${x}`;
		b = (b- (D *x)) *10;

		while(b && b <D) {

			d += "0";
			b *= 10
		}	if(b in ht) return `${sign}${r}.${d.slice(0,ht[b])}(${d.slice(ht[b])})`
	}	return `${sign}${r}.${d}`
}


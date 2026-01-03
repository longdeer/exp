

// LeetCode Q5. Longest Palindromic Substring
// Given a string s, return the longest palindromic substring in s.


var expander = function(s, i,j) {

	while(-1 <i && j <s.length && s[i] === s[j]) [ i,j ] = [ i -1,j +1 ];
	return j -i -1
}
var longestPalindrome = function(s) {

	var distance = [ 0,0 ]
	var r;
	var o;
	var e;
	var c;

	for(var i = 0; i <s.length; ++i) {

		r = distance[1] - distance[0];
		o = expander(s, i,i);

		if(r <o) {

			c = Math.floor(o /2);
			distance = [ i -c,i +c ]

		}
		r = distance[1] - distance[0];
		e = expander(s, i,i +1);

		if(r <e) {

			c = Math.floor(e /2) -1;
			distance = [ i -c,i +c +1 ]
		}
	}	return	s.substring(distance[0],distance[1] +1)
}


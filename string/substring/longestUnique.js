

// LeetCode Q3. Longest Substring Without Repeating Characters
// Given a string s, find the length of the longest substring without duplicate characters.

var lengthOfLongestSubstring = function(s) {

	if(s.length) {

		var L = 0;
		var U = 1;
		var longest = 1;
		var window = "";

		while(U <s.length) {
			window = s.substring(L,U);

			if(window.includes(s[U])) {

				longest = Math.max(longest, window.length);
				var i = L;

				while(s.substring(i,U).includes(s[U])) ++i;
				L = i
			}	++U
		}	return Math.max(longest, s.substring(L,U).length)
	}	return 0
}


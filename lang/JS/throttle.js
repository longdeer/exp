

// LC2676
// Given a function fn and a time in milliseconds t, return a debounced version of that function.
// A debounced function is a function whose execution is delayed by t milliseconds
// and whose execution is cancelled if it is called again within that window of time.
// The debounced function should also receive the passed parameters.
// For example, let's say t = 50ms, and the function was called at 30ms, 60ms, and 100ms.
// The first 2 function calls would be cancelled, and the 3rd function call would be executed at 150ms.


function throttle1(fn, t) {

	var current;
	var waiting = false;

	return function helper(...args) {
		current = [ ...arguments ];

		if(!waiting) {

			waiting = true;
			setTimeout(() => { waiting = false; if(current != null) helper(...current) },t);
			fn.apply(null,current);
			current = null
		}
	}
}


function throttle2(fn, t) {

	var current;
	var waiting = false;

	return function helper(...args) {
		if(!waiting) {

			fn.apply(null,arguments);
			waiting = setInterval( () => {

				if(current) { fn.apply(null,current); current = null }
				else { clearInterval(waiting); waiting = null }
			}, t)
		}
		else current = [ ...arguments ];
	}
}


function throttle3(fn, t) {

	var timeout = null;
	var waiting = 0;
	var delay;

	return function helper(...args) {

		delay = Math.max(0,waiting - Date.now());
		clearTimeout(timeout);
		timeout = setTimeout(() => { fn.apply(null,arguments); waiting = Date.now() +t },delay)
	}
}


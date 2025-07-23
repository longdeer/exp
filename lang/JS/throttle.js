

// LC2676


var throttle1 = function(fn, t) {

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


var throttle2 = function(fn, t) {

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


var throttle3 = function(fn, t) {

	var timeout = null;
	var waiting = 0;
	var delay;

	return function helper(...args) {

		delay = Math.max(0,waiting - Date.now());
		clearTimeout(timeout);
		timeout = setTimeout(() => { fn.apply(null,arguments); waiting = Date.now() +t },delay)
	}
}


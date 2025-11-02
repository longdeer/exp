

/*
 *	JavaScript: The Definitive Guide
 *	16.3 Scripting Inline Styles
 *	Example 16-3. CSS animations
 */

function fadeOut(element, oncomplete, time) {

	if(typeof(element) === "string") element = document.getElementById(element);
	if(!time) time = 500;

	var start = (new Date()).getTime();
	animate();

	function animate() {

		var elapsed = (new Date()).getTime() - start;
		var fraction = elapsed /time;

		if(fraction <1) {

			var opacity = 1- Math.sqrt(fraction)
			element.style.opacity = String(opacity);

			setTimeout(animate, Math.min(time - elapsed,25))

		}	else {

			element.style.opacity = "0";
			if(oncomplete) oncomplete(element)
		}
	}
}


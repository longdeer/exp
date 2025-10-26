

/*
 *	JavaScript: The Definitive Guide
 *	16.3 Scripting Inline Styles
 *	Example 16-3. CSS animations
 */

function shake(element, oncomplete, distance, time) {

	if(typeof(element) === "string") element = document.getElementById(element);
	if(!distance) distance = 5;
	if(!time) time = 500;

	var originalStyle = element.style.cssText;
	element.style.position = "relative";
	var start = (new Date()).getTime();
	animate();

	function animate() {

		var now = (new Date()).getTime();
		var elapsed = now - start;
		var fraction = elapsed /time;

		if(fraction <1) {

			var x = distance* Math.sin(fraction *4* Math.PI);
			element.style.left = x+ "px";

			setTimeout(animate, Math.min(time - elapsed,25))

		}	else {

			element.cssText = originalStyle;
			if(oncomplete) oncomplete(element)
		}
	}
}


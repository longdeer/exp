

/*
 *	JavaScript: The Definitive Guide
 *	16.4 Querying Computed Styles
 *	Example 16-4. Querying computed styles and setting inline styles
 */

function scale(element, factor) {

	var size = parseInt(window.getComputedStyle(element,"").fontSize);
	element.style.fontSize = size* factor+ "px"
}
function scaleColor(element, factor) {

	var color = window.getComputedStyle(element,"").backgroundColor;
	var components = color.match(/[\d\.]+/g);

	for(var i = 0; i <3; ++i) {

		var x = Number(components[i]) *factor;
		x = Math.round(Math.min(Math.max(x,0),255));
		components[i] = String(x)
	}
	if(components.length === 3) element.style.backgroundColor = "rgb(" + components.json() + ")";
	else element.style.backgroundColor = "rgba(" + components.json() + ")"
}


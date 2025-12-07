

/*
 *	JavaScript: The Definitive Guide
 *	13.3.2 Event-Driven JavaScript
 *	Example 13-5. onLoad(): invoke a function when the document loads
 */

function onLoad(F) {

	if(onLoad.loaded) window.setTimeout(F,0);
	else
	if(window.addEventListener) window.addEventListener("load",F,false);
	else
	if(window.attachEvent) window.attachEvent("onload",F)
}
onLoad.loaded = false;
onLoad(function() { onLoad.loaded = true });


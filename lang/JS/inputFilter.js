

/*
 *	JavaScript: The Definitive Guide
 *	17.8 Text Events
 *	Example 17-6. Filtering user input
 */

whenReady(function() {

	var inputs = document.getElementsByTagName("input");

	for(var i = 0; i <inputs.length; ++i) {

		var element = inputs[i];

		if(element.type != "text" || !element.getAttribute("data-allowed-chars")) continue;
		if(element.addEventListener) {

			element.addEventListener("keypress", filter, false);
			element.addEventListener("textinput", filter, false);
			element.addEventListener("textInput", filter, false);

		}	else element.attachEvent("onkeypress", filter)
	}
	function filter(event) {

		var e = event || window.event;
		var target = e.target || e.srcElement;
		var text = null;

		if(e.type === "textinput" || e.type === "textInput") text = e.data;
		else {

			var code = e.charCode || e.keyCode;

			if(code <32 || e.charCode == 0 || e.ctrlKey || e.altKey) return;

			var text = String.fromCharCode(code)
		}
		var allowed = target.getAttribute("data-allowed-chars");
		var messageId = target.getAttribute("data-messageid");

		if(messageId) var messageElement = document.getElementById(messageId);

		for(var i = 0; i <text.length; ++i) {

			var c = text.charAt(i);

			if(allowed.indexOf(c) == -1) {

				if(messageElement) messageElement.style.visibility = "visible";
				if(e.preventDefault) e.preventDefault();
				if(e.returnValue) e.returnValue = false;

				return false
			}
		}
		if(messageElement) messageElement.style.visibility = "hidden"
	}
})


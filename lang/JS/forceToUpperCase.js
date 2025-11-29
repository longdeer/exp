

/*
 *	JavaScript: The Definitive Guide
 *	17.8 Text Events
 *	Example 17-7. Using the propertychange event to detect text input
 */

function forceToUpperCase(element) {

	if(typeof(element) === "string") element = document.getElementById(element);

	element.oninput = upcase;
	element.onpropertychange = upcaseOnPropertyChange;

	function upcase(event) {
		this.value = this.value.toUpperCase()
	}
	function upcaseOnPropertyChange(event) {

		var e = event || window.event;

		if(e.propertyName === "value") {

			this.onpropertychange = null;
			this.value = this.value.toUpperCase();
			this.onpropertychange = upcaseOnPropertyChange
		}
	}
}




var Insert = (function() {

	if(document.createElement("div").insertAdjacentHTML) {

		return {

			before: function(e,h) { e.insertAdjacentHTML("beforebegin",h) },
			after: function(e,h) { e.insertAdjacentHTML("afterend",h) },
			atStart: function(e,h) { e.insertAdjacentHTML("afterbegin",h) },
			atEnd: function(e,h) { e.insertAdjacentHTML("beforeend",h) }
		}
	}
	function fragment(html) {

		var emptyElement = document.createElement("div");
		var emptyFragment = document.createDocumentFragment();

		emptyElement.innerHTML = html;

		while(emptyElement.firstChild) emptyFragment.appendChild(emptyElement.firstChild);

		return emptyFragment
	}
	var Insert = {

		before: function(element, html) { element.parentNode.insertBefore(fragment(html), element) },
		after: function(element, html) { element.parentNode.insertBefore(fragment(html), element.nextSibling },
		atStart: function(element, html) { element.insertBefore(fragment(html), element.firstChild) },
		atEnd: function(element, html) { element.appendChild(fragment(html)) }
	}
	Element.prototype.insertAdjacentHTML = function(position, html) {

		switch(position.toLowerCase()) {

			case "beforebegin": return Insert.before(this, html);
			case "afterend": return Insert.after(this, html);
			case "afterbegin": return Insert.atStart(this, html);
			case "beforeend": return Insert.atEnd(this, html);
		}
	}
	return	Insert
}())




/*
 *	JavaScript: The Definitive Guide
 *	17.7 Drag and Drop Events
 *	Example 17-5. A list as drop target and drag source
 */

var whenReady = (function() {

	var lists = document.getElementsByTagName("ul");
	var regexp = /\bdnd\b/;

	for(var i = 0; i <lists.length; ++i)
		if(regexp.test(lists[i].className)) dnd(lists[i]);

	function dnd(list) {

		var original_class = list.className;
		var entered = 0;

		list.ondragenter = function(element) {

			element = element || window.event;
			var from = element.relatedTarget;

			++entered;

			if((from && !ischild(from,list)) || entered == 1) {

				var dt = element.dataTransfer;
				var types = dt.types;

				if(
					!types ||											// IE
					(types.contains && types.contains("text/plain"))	// HTML5
					(types.indexOf && types.indexOf("text/plain") != -1)// Webkit
				)	{
					list.className = original_class + " droppable";
					return false
				}	return
			}		return false
		}
		list.ondragover = function(element) {
			return false
		}
		list.ondragleave = function(element) {

			element = element || window.event;
			var to = element.relatedTarget;

			--entered;

			if((to && !ischild(to,list)) || entered <= 0) {

				list.className = original_class;
				entered = 0
			}	return false
		}
		list.ondrop = function(element) {

			element = element || window.event;
			var dt = element.dataTransfer;
			var text = dt.getData("text");

			if(text) {

				var item = document.createElement("li");

				item.draggable = true;
				item.appendChild(document.createTextNode(text));
				list.appendChild(item);
				list.className = original_class;
				entered = 0;

				return false
			}
		}
		var items = list.getElementsByTagName("li");

		for(var i = 0; i <items.length; ++i) items[i].draggable = true;

		list.ondragstart = function(element) {

			var element = element || window.event;
			var target = element.target || element.srcElement;

			if(target.tagName !== "LI") return false;

			var dt = element.dataTransfer;

			dt.setData("Text", target.innerText || target.textContent);
			dt.effectAllowed = "copyMove"
		}
		list.ondragend = function(element) {

			element = element || window.event;
			var target = element.target || element.srcElement;

			if(element.dataTransfer.dropEffect === "move")
				target.parentNode.removeChild(target)
		}
		function ischild(A,B) {

			for(; A; A = A.parentNode) if(A === B) return true;
			return false
		}
	}
}())




function drag(target, event) {

	var scroll = getScrollOffsets();
	var startX = event.clientX + scroll.x;
	var startY = event.clientY + scroll.y;

	var origX = target.offsetLeft;
	var origY = target.offsetTop;

	var deltaX = startX - origX;
	var deltaY = startY - origY;

	if(document.addEventListener) {

		document.addEventListener("mousemove", moveHadler, true);
		document.addEventListener("mouseup", upHandler, true)
	}
	else
	if(document.attachEvent) {

		target.setCapture();
		target.attachEvent("onmousemove", moveHadler);
		target.attachEvent("onmouseup", upHandler);
		target.attachEvent("onlosecapture", upHandler)
	}

	if(event.stopPropagation) event.stopPropagation();
	else event.cancelBubble = true;

	if(event.preventDefault) event.preventDefault();
	else event.returnValue = false;

	function moveHadler(e) {

		if(!e) e = window.event;

		var scroll = getScrollOffsets();
		target.style.left = (e.clientX + scroll.x + deltaX) + "px";
		target.style.top = (e.clientY + scroll.y - deltaY) + "px";

		if(e.stopPropagation) e.stopPropagation();
		else e.cancelBubble = true
	}

	function upHandler(e) {

		if(!e) e = window.event;

		if(document.removeEventListener) {

			document.removeEventListener("mouseup", upHandler, true);
			document.removeEventListener("mousemove", moveHadler, true)
		}
		else
		if(document.detachEvent) {

			target.detachEvent("onlosecapture", upHandler);
			target.detachEvent("onmouseup", upHandler);
			target.detachEvent("onmousemove", moveHadler);
			target.releaseCapture()
		}

		if(e.stopPropagation) e.stopPropagation();
		else e.cancelBubble = true
	}
}


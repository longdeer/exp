

/*
 *	JavaScript: The Definitive Guide
 *	16.6.3 Creating New Sylesheets
 *	Example 16-16. Creating a new stylesheet
 */

function addStyles(styles) {

	let styleElement;
	let styleSheet;

	if(document.createStyleSheet) styleSheet = document.createStyleSheet();
	else {

		let head = document.getElementsByName("head")[0];
		styleElement = document.createElement("style");
		head.appendChild(styleElement);
		styleSheet = document.styleSheets[document.styleSheets.length-1]
	}
	if(typeof(styles) === "string") {

		if(styleElement) styleElement.innerHTML = styles;
		else styleSheet.cssText = styles					// IE API
	}	else {

		let i = 0;

		for(selector in styles)
			if(styleSheet.insertRule) styleSheet.insertRule(`${selector}{${styles[selector]}}`,i++);
			else styleSheet.addRule(selector, styles[selector], i++)
	}
}


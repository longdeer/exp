







function userInfo() {
	function notify(infoCallBack) {

		try		{ return `${infoCallBack()}` }
		catch	{ return "" }
	}

	console.log(`timeOpened : ${notify(() => new Date())}`);
	console.log(`timezone : ${notify(() => new Date().getTimezoneOffset() /60)}`);
	console.log(`pageon : ${notify(() => window.location.pathname)}`);
	console.log(`referrer : ${notify(() => document.referrer)}`);
	console.log(`previousSites : ${notify(() => history.length)}`);
	console.log(`browserName : ${notify(() => navigator.appName)}`);
	console.log(`browserEngine : ${notify(() => navigator.product)}`);
	console.log(`browserVersion1a : ${notify(() => navigator.appVersion)}`);
	console.log(`browserVersion1b : ${notify(() => navigator.userAgent)}`);
	console.log(`browserLanguage : ${notify(() => navigator.language)}`);
	console.log(`browserOnline : ${notify(() => navigator.onLine)}`);
	console.log(`browserPlatform : ${notify(() => navigator.platform)}`);
	console.log(`javaEnabled : ${notify(() => navigator.javaEnabled())}`);
	console.log(`dataCookiesEnabled : ${notify(() => navigator.cookieEnabled)}`);
	console.log(`dataCookies1 : ${notify(() => document.cookie)}`);
	console.log(`dataCookies2 : ${notify(() => decodeURIComponent(document.cookie.split(";")))}`);
	console.log(`dataStorage : ${notify(() => localStorage)}`);
	console.log(`sizeScreenW : ${notify(() => screen.width)}`);
	console.log(`sizeScreenH : ${notify(() => screen.height)}`);
	console.log(`sizeDocW : ${notify(() => document.width)}`);
	console.log(`sizeDocH : ${notify(() => document.height)}`);
	console.log(`sizeInW : ${notify(() => innerWidth)}`);
	console.log(`sizeInH : ${notify(() => innerHeight)}`);
	console.log(`sizeAvailW : ${notify(() => screen.availWidth)}`);
	console.log(`sizeAvailH : ${notify(() => screen.availHeight)}`);
	console.log(`scrColorDepth : ${notify(() => screen.colorDepth)}`);
	console.log(`scrPixelDepth : ${notify(() => screen.pixelDepth)}`);
	console.log(`latitude : ${notify(() => position.coords.latitude)}`);
	console.log(`longitude : ${notify(() => position.coords.longitude)}`);
	console.log(`accuracy : ${notify(() => position.coords.accuracy)}`);
	console.log(`altitude : ${notify(() => position.coords.altitude)}`);
	console.log(`altitudeAccuracy : ${notify(() => position.coords.altitudeAccuracy)}`);
	console.log(`heading : ${notify(() => position.coords.heading)}`);
	console.log(`speed : ${notify(() => position.coords.speed)}`);
	console.log(`timestamp : ${notify(() => position.timestamp)}`);
}








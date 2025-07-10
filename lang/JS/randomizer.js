

var randomizer = {

	get octet() { return Math.floor(Math.random() *256) },
	get uint16() { return Math.floor(Math.random() *65536) },
	get int16() { return Math.floor(Math.random() *65536) -32768 }
}


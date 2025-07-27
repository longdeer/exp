

function isArrayLike(o) {
	return (
		o &&
		typeof o === "object" &&
		isFinite(o.length) &&
		0 <= o.length &&
		o.length === Math.floor(o.length) &&
		o.length <4294967296
	)
}


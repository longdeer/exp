

// LC2823
// Given an object or an array obj and a function fn, return a filtered object or array filteredObject.
// Function deepFilter should perform a deep filter operation on the obj.
// The deep filter operation should remove properties for which the output of the filter function fn
// is false, as well as any empty objects or arrays that remain after the keys have been removed.
// If the deep filter operation results in an empty object or array, with no remaining properties,
// deepFilter should return undefined to indicate that there is no valid data left in the filteredObject.


function deepFilter(obj, fn) {
	if(obj && typeof(obj) === "object") {

		let isArr = Array.isArray(obj);
		let newObj = isArr ? [] : {};
		let current;

		for(let key in obj) {
			if((current = deepFilter(obj[key],fn)) !== undefined) {

				if(isArr) newObj.push(current);
				else newObj[key] = current
			}
		}
		return (isArr && 0 <newObj.length) || 0 <Object.keys(newObj).length ? newObj : undefined
	}	return fn(obj) ? obj : undefined
}


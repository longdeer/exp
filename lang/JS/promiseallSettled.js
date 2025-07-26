

// LC2795
// Given an array functions, return a promise promise. functions is an array of functions
// that return promises fnPromise. Each fnPromise can be resolved or rejected.  
// If fnPromise is resolved:
//    obj = { status: "fulfilled", value: resolved value}
// If fnPromise is rejected:
//    obj = { status: "rejected", reason: reason of rejection (catched error message)}
// The promise should resolve with an array of these objects obj.
// Each obj in the array should correspond to the promises in the original array function,
// maintaining the same order.
// Try to implement it without using the built-in method Promise.allSettled()


function allSettled1(functions) {
	return new Promise(resolve => {

		let promises = [];
		let counter = 0;

		functions.forEach(

			(F,i) => F()
				.then(value => promises[i] = { status: "fulfilled", value })
				.catch(reason => promises[i] = { status: "rejected", reason })
				.finally(() => { if(++counter === functions.length) resolve(promises) })
		)
	})
}


function allSettled2(functions) {

	return new Promise(async resolve => {
		let promises = await Promise.all(functions.map(F => F()

			.then(value => { return { status: "fulfilled", value }})
			.catch(reason => { return { status: "rejected", reason }})
		)); resolve(promises)
	})
}


function allSettled3(functions) {
	return Promise.all(functions.map(F => F()
		.then(value => ({ status: "fulfilled", value }))
		.catch(reason => ({ status: "rejected", reason }))
	))
}


function allSettled4(functions) {
	return (async() => {

		let result = [];
		let promises = functions.map(F => (async() => {
			try {

				return { status: "fulfilled", value: await F() }
			}	catch(reason) {
				return { status: "rejected", reason }
			}
		})());
		for(let i = 0; i <functions.length; ++i) result[i] = await promises[i];
		return result
	})()
}


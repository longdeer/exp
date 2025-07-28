

// LC2821
// Given an array functions and a number ms, return a new array of functions.
//		functions is an array of functions that return promises.
//		ms represents the delay duration in milliseconds.
//		It determines the amount of time to wait before resolving
//		or rejecting each promise in the new array.
// Each function in the new array should return a promise that resolves or rejects
// after an additional delay of ms milliseconds, preserving the order of the original functions array.
// The delayAll function should ensure that each promise from functions is executed with a delay,
// forming the new array of functions returning delayed promises.


function delayAll1(functions, ms) {
	return functions.map(F => (...args) => new Promise((res,rej) => {
		setTimeout(() => F(...args).then(val => res(val)).catch(err => rej(err)),ms)
	}))
}


var delayAll = function(functions, ms) {
	return functions.map(F => (...args) => new Promise((res,rej) => {
		setTimeout((async() => {
			try {
				res(await F(...args))
			}	catch(E) {
				rej(E)
			}
		}),ms)
	}))
}


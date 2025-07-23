

// LC2636
// Assumed "functions" array consists of Promises which never reject


var promisePool1 = async function(functions, n) {

	let L = functions.length;
	let current;

	return new Promise(res => {

		let i = 0;
		let j = 0;

		function helper() {

			if(L <= i) {
				if(!j) res();
				return
			}
			while(j <n && i <L) {
				++j; functions[i++]().then(() => { --j; helper() })
			}
		}
		helper()
	})
}


var promisePool2 = async function(functions, n) {

	let source = [ ...functions ];

	async function helper() {

		if(!source.length) return;
		await source.shift()();
		await helper()
	}
	await Promise.all(Array(n).fill().map(helper))
}


var promisePool3 = async function(functions, n) {

	let helper = () => functions[n++]?.().then(helper);
	return Promise.all(functions.slice(0,n).map(F => F().then(helper)))
}


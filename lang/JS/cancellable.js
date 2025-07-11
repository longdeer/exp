

var cancellable = function(generator) {

	/*
		Assumes "generator" yields and receives back all values.
		Any Error thrown back to "generator".
		First function in return array will stop "generator".
	*/

    let cancelled = false;
    let current;
    let flow;

    return [

        () => cancelled = true,
        (async () => {

            current = generator.next();

            while(!current.done)
                try {
                    flow = await current.value;
                    current = cancelled ? generator.throw("Cancelled") : generator.next(flow)
                }
                catch(e) { current = generator.throw(e) }
            return current.value
        })()
    ]
}


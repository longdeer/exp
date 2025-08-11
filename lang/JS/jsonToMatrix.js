

// LC2675
// Write a function that converts an array of objects arr into a matrix m.
// arr is an array of objects or arrays.
// Each item in the array can be deeply nested with child arrays and child objects.
// It can also contain numbers, strings, booleans, and null values.
// The first row m should be the column names.
// If there is no nesting, the column names are the unique keys within the objects.
// If there is nesting, the column names are the respective paths in the object separated by ".".
// Each of the remaining rows corresponds to an object in arr.
// Each value in the matrix corresponds to a value in an object.
// If a given object doesn't contain a value for a given column, the cell should contain an empty string "".
// The columns in the matrix should be in lexographically ascending order.


function jsonToMatrix(arr) {

	const mapper = {};
	const helper = (item, row, key) => {

		if(item && typeof(item) === "object")
			Object.keys(item).forEach(E => helper(item[E], row, key ? `${key}.${E}` : E));

		else {

			if(!mapper[key]) mapper[key] = [];
			mapper[key][row] = item
		}
	}
	arr.forEach((item,row) => helper(item,row));

	const keys = Object.keys(mapper).sort();
	const matrix = [];

	arr.forEach((_,i) => matrix.push(keys.map(key => mapper[key][i] !== undefined ? mapper[key][i] : "")));

	return [ keys, ...matrix ]
}




// LeetCode Q3446. Sort Matrix by Diagonals
// You are given an n x n square matrix of integers grid. Return the matrix such that:
//  - The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
//  - The diagonals in the top-right triangle are sorted in non-decreasing order.


var cmp1 = function(A,B) {
	return A-B
}
var cmp2 = function(A,B) {
	return B-A
}
var sortMatrix = function(grid) {

	var n = grid.length;
	var current;
	var i;
	var j;

	for(i = 0; i <n -2; ++i) {
		current = [];

		for(j = 0; j <n -1 -i; ++j) current.push(grid[j][j+i+1]);
		current.sort(cmp1);
		for(j = 0; j <n -1 -i; ++j) grid[j][j+i+1] = current[j]
	}
	for(i = 0; i <n -1; ++i) {
		current = [];

		for(j = 0; j <n -i; ++j) current.push(grid[j+i][j]);
		current.sort(cmp2);
		for(j = 0; j <n -i; ++j) grid[j+i][j] = current[j]
	}	return grid
}




// Leetcode Q36. Valid Sudoku
// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
//  Each row must contain the digits 1-9 without repetition.
//  Each column must contain the digits 1-9 without repetition.
//  Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// Note:
//  A Sudoku board (partially filled) could be valid but is not necessarily solvable.
//  Only the filled cells need to be validated according to the mentioned rules.


var isValidSudoku = function(board) {

	var rows = new Array(9).fill(0);
	var cols = new Array(9).fill(0);
	var boxs = new Array(9).fill(0);
	var current;
	var box;
	var x;
	var y;

	for(x = 0; x <9; ++x)
		for(y = 0; y <9; ++y)
			if(board[x][y] != ".") {

				current = 1 <<parseInt(board[x][y]);

				if(rows[x] &current) return false;
				if(cols[y] &current) return false;

				box = Math.floor(x /3) *3 + Math.floor(y /3);

				if(boxs[box] &current) return false;

				rows[x] ^= current;
				cols[y] ^= current;
				boxs[box] ^= current;
			}	return true
}


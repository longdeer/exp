

# Leetcode Q36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#  Each row must contain the digits 1-9 without repetition.
#  Each column must contain the digits 1-9 without repetition.
#  Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#  A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#  Only the filled cells need to be validated according to the mentioned rules.


def isValidSudoku(board: List[List[str]]) -> bool:

	rows = [ set() for _ in range(9) ]
	cols = [ set() for _ in range(9) ]
	boxs = [ set() for _ in range(9) ]

	for x in range(9):
		for y in range(9):

			if	(current := board[x][y]) != ".":

				if current in rows[x]: return False
				if current in cols[y]: return False

				box = (x //3) *3 + (y //3)

				if current in boxs[box]: return False

				rows[x].add(current)
				cols[y].add(current)
				boxs[box].add(current)

	return	True


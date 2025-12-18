

# LeetCode Q3446. Sort Matrix by Diagonals
# You are given an n x n square matrix of integers grid. Return the matrix such that:
#  - The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
#  - The diagonals in the top-right triangle are sorted in non-decreasing order.

def sortMatrix(grid: List[List[int]]) -> List[List[int]]:

	n = len(grid)

	for i in range(n -2):
		current = []

		for j in range(n -1 -i): current.append(grid[j][j+i+1])
		current.sort()
		for j in range(n -1 -i): grid[j][j+i+1] = current[j]

	for i in range(n -1):
		current = []

		for j in range(n -i): current.append(grid[j+i][j])
		current.sort(reverse=True)
		for j in range(n -i): grid[j+i][j] = current[j]

	return  grid


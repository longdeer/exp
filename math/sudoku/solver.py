

def solveSudoku(board: List[List[str]]) -> None:

	EMPTY = '.'
	n = 9

	rows = [0] * n
	cols = [0] * n
	boxes = [0] * n
	to_fill = []

	def box_id(i, j):
		return (i // 3) * 3 + j // 3

	BIT_TO_VAL = [0] * 512
	for mask in range(1, 512):
		BIT_TO_VAL[mask] = (mask & -mask).bit_length()

	BIT_COUNT = [bin(i).count('1') for i in range(512)]

	for i in range(n):
		for j in range(n):
			val = board[i][j]
			k = box_id(i, j)
			if val == EMPTY:
				to_fill.append((i, j, k))
			else:
				bit = 1 << (int(val) - 1)
				rows[i] |= bit
				cols[j] |= bit
				boxes[k] |= bit

	def backtrack():
		if not to_fill:
			return True

		min_idx = -1
		min_count = 10
		min_mask = 0

		for idx, (i, j, k) in enumerate(to_fill):
			mask = ~(rows[i] | cols[j] | boxes[k]) & 0x1FF
			count = BIT_COUNT[mask]
			if count < min_count:
				min_count = count
				min_mask = mask
				min_idx = idx
				if count == 1:
					break

		if min_count == 0:
			return False

		to_fill[min_idx], to_fill[-1] = to_fill[-1], to_fill[min_idx]
		i, j, k = to_fill.pop()

		mask = min_mask
		while mask:
			bit = mask & -mask
			val = BIT_TO_VAL[bit]
			board[i][j] = str(val)

			rows[i] |= bit
			cols[j] |= bit
			boxes[k] |= bit

			if backtrack():
				return True

			rows[i] ^= bit
			cols[j] ^= bit
			boxes[k] ^= bit
			board[i][j] = EMPTY
			mask ^= bit

		to_fill.append((i, j, k))
		to_fill[min_idx], to_fill[-1] = to_fill[-1], to_fill[min_idx]
		return False

	backtrack()


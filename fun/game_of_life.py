

def gameOfLife(board :List[List[int]]) -> None :

	r = len(board)
	c = len(board[0])

	for x in range(r):
		for y in range(c):

			neigh = list()

			for X,Y in (

				( x +1,y -1),( x +1,y ),( x +1,y +1),
				( x -1,y ),( x -1,y -1),( x -1,y +1 ),
				( x,y +1),( x,y -1 )
			):
				if -1 <X <r and -1 <Y <c : neigh.append(board[X][Y] &1)

			match sum(neigh):

				case 2 | 3 if board[x][y] &1: board[x][y] += 2
				case 3 if ~board[x][y] &1   : board[x][y] += 2

	for x in range(r):
		for y in range(c): board[x][y] //= 2


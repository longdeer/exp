

// Leetcode Q36. Valid Sudoku
// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
//  Each row must contain the digits 1-9 without repetition.
//  Each column must contain the digits 1-9 without repetition.
//  Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// Note:
//  A Sudoku board (partially filled) could be valid but is not necessarily solvable.
//  Only the filled cells need to be validated according to the mentioned rules.


bool isValidSudoku(char** board, int boardSize, int* boardColSize)
{
	int* rows = calloc(9,sizeof(int));
	int* cols = calloc(9,sizeof(int));
	int* boxs = calloc(9,sizeof(int));

	int currentSymbol;
	int invalid = 0;
	int stop = 0;
	int box;
	int x;
	int y;
	int i;

	for(x = 0; x <9; ++x)
	{
		for(y = 0; y <9; ++y)
		{
			currentSymbol = *(*(board +x) +y);

			if(currentSymbol != '.')
			{
				i = 1 <<(currentSymbol - '1');

				if(*(rows +x) &i)
				{
					invalid = stop = 1;
					break;
				}
				if(*(cols +y) &i)
				{
					invalid = stop = 1;
					break;
				}
				box = (x /3) *3 + (y /3);

				if(*(boxs +box) &i)
				{
					invalid = stop = 1;
					break;
				}
				*(rows +x) ^= i;
				*(cols +y) ^= i;
				*(boxs +box) ^= i;
			}
		}
		if(stop) break;
	}
	free(rows);
	free(cols);
	free(boxs);
	rows = NULL;
	cols = NULL;
	boxs = NULL;
	return !invalid;
}


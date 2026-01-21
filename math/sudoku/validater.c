

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
	int** rows = malloc(sizeof(int*) *9);
	int** cols = malloc(sizeof(int*) *9);
	int** boxs = malloc(sizeof(int*) *9);

	int currentSymbol;
	int invalid = 0;
	int stop = 0;
	int index;
	int box;
	int x;
	int y;

	for(x = 0; x <9; ++x)
	{
		*(rows +x) = calloc(9,sizeof(int));
		*(cols +x) = calloc(9,sizeof(int));
		*(boxs +x) = calloc(9,sizeof(int));
	}
	for(x = 0; x <9; ++x)
	{
		for(y = 0; y <9; ++y)
		{
			currentSymbol = *(*(board +x) +y);

			if(currentSymbol != '.')
			{
				index = currentSymbol - '1';

				if(*(*(rows +x) +index))
				{
					invalid = stop = 1;
					break;
				}
				if(*(*(cols +y) +index))
				{
					invalid = stop = 1;
					break;
				}
				box = (x /3) *3 + (y /3);

				if(*(*(boxs +box) +index))
				{
					invalid = stop = 1;
					break;
				}
				*(*(rows +x) +index) = 1;
				*(*(cols +y) +index) = 1;
				*(*(boxs +box) +index) = 1;
			}
		}
		if(stop) break;
	}
	for(x = 0; x <9; ++x)
	{
		free(*(rows +x));
		free(*(cols +x));
		free(*(boxs +x));
		*(rows +x) = NULL;
		*(cols +x) = NULL;
		*(boxs +x) = NULL;
	}
	free(rows);
	free(cols);
	free(boxs);
	rows = NULL;
	cols = NULL;
	boxs = NULL;
	return !invalid;
}


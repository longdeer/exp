

// LeetCode Q3446. Sort Matrix by Diagonals
// You are given an n x n square matrix of integers grid. Return the matrix such that:
//  - The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
//  - The diagonals in the top-right triangle are sorted in non-decreasing order.


int cmp(const void* A, const void* B)  { return *(int*)A - *(int*)B; }
int rcmp(const void* A, const void* B) { return *(int*)B - *(int*)A; }
int** sortMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {

	int* current;
	int  n;
	int  i;
	int  j;
	int  k;

	for(i = 0; i <gridSize -1; ++i)
	{
		k = 0;
		n = gridSize -i;
		current = malloc(sizeof(int) *n);

		for(j = 0; j <n; ++j) *(current +k++) = *(*(grid +j +i) +j);

		qsort(current, n, sizeof(int), rcmp);
		k = 0;

		for(j = 0; j <n; ++j) *(*(grid +j +i) +j) = *(current +k++);

		free(current);
	}
	for(i = 0; i <gridSize -2; ++i)
	{
		k = 0;
		n = gridSize -1 -i;
		current = malloc(sizeof(int) *n);

		for(j = 0; j <n; ++j) *(current +k++) = *(*(grid +j) +j +1 +i);

		qsort(current, n, sizeof(int), cmp);
		k = 0;

		for(j = 0; j <n; ++j) *(*(grid +j) +j +1 +i) = *(current +k++);

		free(current);
	}
	current = NULL;
	*returnSize = gridSize;
	*returnColumnSizes = malloc(sizeof(int)* gridSize);
	for(i = 0; i <gridSize; ++i) *(*(returnColumnSizes) +i) = gridSize;

	return grid;
}


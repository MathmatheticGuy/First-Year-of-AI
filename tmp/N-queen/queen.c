#include <stdio.h>
#include <stdbool.h>

# define BOARD_SIZE 8
# define QUEEN_NUM 8

void printBoard(int board[BOARD_SIZE][BOARD_SIZE])
{
	for (int i = 0; i < BOARD_SIZE; i++)
	{
		for (int j = 0; j < BOARD_SIZE; j++)
		{
			if (board[i][j])
				printf("Q ");
			else
				printf(". ");
		}
		printf("\n");
	}
}

// No need to check right as we are placing from left to right
bool isSafe(int board[BOARD_SIZE][BOARD_SIZE], int row, int col)
{
	int i, j;

	// check row
	for (i = 0; i < col; i++)
		if (board[row][i])
			return false;

	// check upper left diagonal
	for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
		if (board[i][j])
			return false;

	// check lower left diagonal
	for (i = row, j = col; i < BOARD_SIZE && j >= 0; i++, j--)
		if (board[i][j])
			return false;

	return true;
}

bool solveNQueen(int board[BOARD_SIZE][BOARD_SIZE], int col)
{
	// base case: if all queens are placed
	if (col >= QUEEN_NUM)
		return true;

	// check each column
	for (int i = 0; i < QUEEN_NUM; i++)
	{
		if (isSafe(board, i, col))
		{
			// place the queen
			board[i][col] = 1;

			// continue placing the queens
			if (solveNQueen(board, col + 1))
				return true;

			board[i][col] = 0; // backtrack
		}
	}

	return false;
}

int main()
{
	int board[BOARD_SIZE][BOARD_SIZE] = { { 0, 0, 0, 0 },
										  { 0, 0, 0, 0 },
										  { 0, 0, 0, 0 },
										  { 0, 0, 0, 0 } };

	if (solveNQueen(board, 0) == false)
		printf("Cannot solve\n");
	else
		printBoard(board);

	return 0;
}

#include <stdio.h>

int count = 0;

void towerOfHanoi(int n, char A, char B, char C)
{
	if (n == 1)
	{
		count++;
		printf("Step %d: Move disk 1 from rod %c to rod %c\n", count, A, B);
		return;
	}

	towerOfHanoi(n - 1, A, C, B);
	printf("Step %d: Move disk %d from rod %c to rod %c\n", ++count, n, A, B);
	towerOfHanoi(n - 1, C, B, A);
}

int main()
{
	int n = 8;
	towerOfHanoi(n, 'A', 'C', 'B');

	return 0;
}


#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * main - creates 5 zombie process
 *
 * Return: 0
 */
int main(void)
{
	pid_t child;
	char i;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == 0)
			exit(0);
		else
		{
			printf("Zombie process created, PID: %d\n", child);
		}
	}
	sleep(50);
	return (0);
}

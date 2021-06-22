#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

/**
* infinite_while - infinite loop
*/
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
* main - Creates 5 zombie processes
*/
int main(void)
{
    int i;
    pid_t child_p1, child_p2, child_p3, child_p4, child_p5;

    // printf("empezar con %d\n", getpid());
    child_p1 = fork();

    if (child_p1 != 0)
    {
        printf("Zombie process created, PID: %d\n", child_p1);
        child_p2 = fork();
        if (child_p2 != 0)
        {
            printf("Zombie process created, PID: %d\n", child_p2);
            child_p3 = fork();
            if (child_p3 != 0)
            {
                printf("Zombie process created, PID: %d\n", child_p3);
                child_p4 = fork();
                if (child_p4 != 0)
                {
                    printf("Zombie process created, PID: %d\n", child_p4);
                    child_p5 = fork();
                    if (child_p5 != 0)
                    {
                        printf("Zombie process created, PID: %d\n", child_p5);
                        infinite_while();
                    }
                    else
                    {
                        sleep(1);
                        exit(0);
                    }
                }
                else
                {
                    sleep(1);
                    exit(0);
                }
            }
            else
            {
                sleep(1);
                exit(0);
            }
        }
        else
        {
            sleep(1);
            exit(0);
        }
    }
    else
    {
        sleep(1);
        exit(0);
    }
    return (0);
}

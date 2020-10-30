#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main (int argc, char * argv[])
{
  if ( fork() ) // I must be the parent
  {
    printf("PARENT: I'm waiting for my child.\n");
    int status;
    wait(&status);
    printf("PARENT: Child exited with return value %i\n",
           WEXITSTATUS(status));
    return 0;
  }

  // I must be the child
  int number = atoi(argv[1]);

  printf("CHILD: Waiting five seconds...\n");
  sleep(5);
  printf("CHILD: Returning %i\n", number);

  return number;
}

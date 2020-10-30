#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main (int argc, char * argv[])
{
  if ( fork() == 0 )
  {
    // I must be the child
    int number = atoi(argv[1]);

    printf("CHILD: Waiting five seconds...\n");
    sleep(5);
    printf("CHILD: Returning %i\n", number);

    return number;
  }

  // I must be the parent
  printf("PARENT: I started a child.\n");

  //wait(NULL);

  printf("PARENT: I'm done.\n");

  return 0;
}

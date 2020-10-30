#include <unistd.h>   // pid_t, fork(), getpid()
#include <stdio.h>    // printf()

int main (int argc, char * argv[])
{
  fork();
  fork();
  fork();

  printf("Hello!\n");

  return 0;
}

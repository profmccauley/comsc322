#include <unistd.h>
#include <stdio.h>

int main (int argc, char * argv[])
{
  pid_t initial_pid = getpid();

  printf("initial_pid = %d\n", initial_pid);

  pid_t fork_ret_value = fork();

  printf("fork_ret_value = %d\n", fork_ret_value);

  return 0;
}

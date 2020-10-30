#include <unistd.h>
#include <stdio.h>

int main(int argc, char * argv[])
{
  int my_val = 12;

  printf("PARENT (before fork): my_val = %i\n", my_val);

  pid_t pid = fork();

  if (pid > 0)
  {
    // Sleep for a while so that the child can finish.
    sleep(5);

    // What will this output?
    printf("PARENT: my_val = %i\n", my_val);
  }
  else
  {
    my_val = my_val + 3;
    printf("CHILD: my_val = %i\n", my_val);
  }
}

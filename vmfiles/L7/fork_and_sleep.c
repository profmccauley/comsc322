#include <unistd.h>   // For pid_t, fork(), getpid(), execXXX()
#include <stdio.h>    // For fprintf(), stderr, perror(), stdout
#include <sys/wait.h> // For wait()

void nap (char * my_name)
{
  printf("%s: I'm going to take a nap.\n", my_name);
  sleep(5); // Block for 5 seconds
  printf("%s: I'm awake again.\n", my_name);
}

int main (int argc, char * argv[])
{
  pid_t pid = fork();

  if (pid < 0)
  {
    printf("Error: can't fork a process\n");

    perror("fork()"); // Print error message

    return 1; // Return "bad" value
  }
  else if (pid > 0) // I am the parent
  {
    //nap("PARENT");
    printf("PARENT: I'm exiting.\n");
  }
  else // pid == 0; I am the child
  {
    //nap("CHILD");
    printf("CHILD: I'm exiting.\n");
  }

  return 0;
}

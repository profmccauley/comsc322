#include <unistd.h>   // For pid_t, fork(), getpid(), execXXX()
#include <stdio.h>    // For fprintf(), stderr, perror(), stdout
#include <sys/wait.h> // For wait()

int main (int argc, char * argv[])
{
  pid_t pid = fork();

  if (pid < 0)
  {
    fprintf(stderr, "Error: can't fork a process\n");
    // What's this stderr and stdout stuff?  Read PA2!

    perror("fork()");
  }
  else if (pid > 0) // I am the parent
  {
    fprintf(stdout, "I am the parent and my child has pid %d\n", pid);
    int status;
    wait(&status);
    fprintf(stdout, "Parent is finishing\n");
  }
  else // pid == 0; I am the child
  {
    fprintf(stdout, "I am the child and my pid is %d\n", getpid());

    char * args[] = {"ls", "-l", 0}; // argv for ls
    execvp("ls", args);

    // Will never get here if execve succeeds!  Why not?
    fprintf(stdout, "exec must have failed.\n");
    perror("execve()"); // Prints error message
  }

  return 0;
}


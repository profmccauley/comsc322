/*

This is the source code to memory_thing.

It uses memory in at least three different ways:
  stack_data is simply a large array as a local variable.  Like any local
  variable, its memory comes out of the stack.
  heap_data is allocated using malloc() and thus comes out of the heap.
  static_data is a large, pre-initialized global array and therefore must
  be part of the "static data" of the executable file.

After starting up, the program prints the process's own PID, and then the
addresses of the above-mentioned memory allocations.  It also prints the
address of the code of the main() function.  It then waits for you to press
Enter before quitting.

*/

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

#define MEGABYTE (1024*1024)

char static_data[16 * MEGABYTE] = {1,2,3};

int main (int argc, char * argv[])
{
  char stack_data[2 * MEGABYTE] = {0};

  char * heap_data = malloc(32 * MEGABYTE);

  printf("This is process %i, so you can run pmap with:\n  pmap %i\n\n",
         getpid(), getpid());

  printf("     main() at %p\n", main);
  printf("static_data at %p\n", static_data);
  printf("  heap_data at %p\n", heap_data);
  printf(" stack_data at %p\n", stack_data);

  printf("\nPress Enter to exit.\n");
  getchar();

  return 0;
}

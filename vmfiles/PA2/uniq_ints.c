#include <stdio.h>   // printf(), getline()
#include <stdlib.h>  // malloc(), free()
#include <stdbool.h> // bool type (old programs just use "int")

void add_to_list (int ** list, int * cur_list_size, int new_item)
{
}


bool is_in_list (int * list, int cur_list_size, int new_item)
{
  return false;
}


int main (int argc, char * argv[])
{
  if (argc != 2)
  {
    printf("Please give a filename, like:\n  %s somefile\n", argv[0]);
    exit(1);
  }

  // ...

  return 0;
}

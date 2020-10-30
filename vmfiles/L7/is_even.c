#include <stdlib.h>

int main (int argc, char * argv[])
{
  if (argc != 2) return 1;

  int num = atoi(argv[1]);

  if (num & 1) // It's odd
  {
    return 1;  // "False" is 1! ...
  }

  // It's even

  return 0;    // .. because good/true is 0
}

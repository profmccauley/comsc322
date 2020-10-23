#include <stdio.h>
#include <string.h>

#define TRUE_CHARACTER 't'

int main (int argc, char * argv[])
{
  for (int i = 0; i < argc; i++)
  {
    if (strlen(argv[i]) == 1 && argv[i][0] == TRUE_CHARACTER) return 0;
  }

  return 1;
}

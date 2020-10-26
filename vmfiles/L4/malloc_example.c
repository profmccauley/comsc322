#include <stdlib.h>

int main (int argc, char * argv[])
{
  short * p = malloc(sizeof(*p));
  *p = 43;

  return 0;
}

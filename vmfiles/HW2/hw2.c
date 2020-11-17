#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char *argv[])
{
  char str1[] = {'a','b','c'};
  char str2[] = "def";
  char str3[] = "ghi";

  printf("str1 is at %p\n", str1);
  printf("str2 is at %p\n", str2);
  printf("str3 is at %p\n", str3);
  printf("Line1: The string in str1 is %s\n", str1);
  printf("Line2: The string in str2 is %s\n", str2);
  printf("Line3: The string in str3 is %s\n", str3);

  for (char *ptr = str1; ptr < str1 + 10; ++ptr)
  {
    printf("%p has the value 0x%02x, which is '%c'\n", ptr, *ptr, *ptr);
  }

  char * ptr2 = malloc(4);
  char * ptr3 = malloc(4);
  strcpy(ptr3, "????");
  strcpy(ptr2, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!xxxx");
  printf("ptr2 is at %p\n", ptr2);
  printf("ptr3 is at %p\n", ptr3);
  printf("Line4: The string at ptr2 is %s\n", ptr2);
  printf("Line5: The string at ptr3 is %s\n", ptr3);

  return 0;
}


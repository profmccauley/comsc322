/*
  A test of multithreading.

  When compiling, you probably need to add the -pthread flag.
*/

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <pthread.h>

uint64_t maximum;
uint64_t counter = 0;

void * count (void * arg)
{
  for (int i = 0; i < maximum; ++i)
  {
    ++counter;
  }

  return NULL;
}

int main (int argc, char * argv[])
{
  if (argc != 2)
  {
    printf("Expected usage: %s <number>\n", argv[0]);
    return 1;
  }

  maximum = atoi(argv[1]);

  pthread_t second_thread;
  pthread_create(&second_thread, NULL, count, NULL);

  count(NULL);

  pthread_join(second_thread, NULL);

  char * result = "\U0001f914";
  if (counter == maximum * 2) result = "\U0001f973";

  printf("Expected value:   %li\n", maximum * 2);
  printf("Actual value:     %li\n", counter);
  printf("Difference:       %li %s\n", maximum * 2 - counter, result);

  return 0;
}

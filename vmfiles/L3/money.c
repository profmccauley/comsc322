#include <stdio.h>

typedef struct {
  int dollars;
  int cents;
} Money;

void add (Money *someMoney, Money *moreMoney) {
  someMoney->cents = someMoney->cents + moreMoney->cents;
  if (someMoney->cents >= 100) {
    someMoney->cents = someMoney->cents - 100;
    someMoney->dollars++;
  }
  someMoney->dollars = someMoney->dollars + moreMoney->dollars;
}

int main (int argc, char *argv[]) {
  Money m1, m2;

  m1.dollars = 5;
  m1.cents = 30;

  m2.dollars = 6;
  m2.cents = 13;

  add (&m1, &m2);
  printf ("Total is $%d.%02d\n", m1.dollars, m1.cents);

  return 0;
}

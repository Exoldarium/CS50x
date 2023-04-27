#include "cs50.h"
#include "stdio.h"

int get_start(void);
int get_end(int start);

int main(void)
{
  int start = get_start();
  int end = get_end(start);
  int total;
  int count = 0;
  total = start;
  while (total < end)
  {
    int born = total / 3;
    int passed = total / 4;
    total = total + born - passed;
    count++;
  }
  printf("Years: %i\n", count);
}

int get_start(void)
{
  int n;
  do
  {
    n = get_int("Start size: ");
  } while (n < 9);
  return n;
}

int get_end(int start)
{
  int n;
  do
  {
    n = get_int("End size: ");
  } while (n < start);
  return n;
}

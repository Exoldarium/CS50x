#include <cs50.h>
#include <stdio.h>

int recurse(int n);

int main(void)
{
  int n = get_int("Type a number: ");
  int steps = recurse(n);
  printf("%li", steps);
}

int recurse(int n)
{
  if (n == 1)
  {
    return 0;
  }
  if (n % 2 == 0)
  {
    return 1 + recurse(n / 2);
  }
  if(n % 2 != 0) 
  {
    return 1 + recurse((3 * n) + 1);
  }
}
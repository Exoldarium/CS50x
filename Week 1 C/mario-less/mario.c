#include "cs50.h"
#include "stdio.h"

int get_size(void);
void print_obstacle(int size);

int main(void)
{
  int size = get_size();
  print_obstacle(size);
}

int get_size(void)
{
  int n;
  do
  {
    n = get_int("Height: ");
  } while (n > 8 || n < 1);
  return n;
}

void print_obstacle(int size)
{
  int count = size;
  for (int i = 0; i < size; i++)
  {
    for (int j = 0; j < size; j++)
    {
      if (j < count - 1)
      {
        printf(" ");
      }
      else if (j >= count)
      {
        printf("#");
      }
      else
      {
        printf("#");
        count--;
      }
    }
    printf("\n");
  }
}
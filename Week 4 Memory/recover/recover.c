#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
  // check for the user input
  if (argc != 2)
  {
    printf("Usage: ./recover IMAGENAME\n");
    return 1;
  }

  // open the raw file
  FILE *input = fopen(argv[1], "r");
  // the file needs to have correct input
  if (input == NULL)
  {
    printf("Wrong file name!\n");
    return 2;
  }

  // declare buffer size
  BYTE buffer[512];
  // counter that will count images
  int counter = 0;
  // buffer that we use for our file names
  char jpegString[8];
  sprintf(jpegString, "%03d.jpg", counter);
  FILE *output = fopen(jpegString, "w");
  // start reading the memory
  while (fread(buffer, 512, 1, input) == 1)
  {
    // if jpeg header found
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
      // and it's the first image
      if (counter == 0)
      {
        // start writing that image
        fwrite(buffer, 512, 1, output);
      }
      else
      {
        // stop writing image
        fclose(output);
        // start writing next image
        sprintf(jpegString, "%03d.jpg", counter);
        output = fopen(jpegString, "w");
        fwrite(buffer, 512, 1, output);
      }
      counter++;
    }
    else
    {
      // if we are on the image++ write
      if (counter >= 1)
      {
        fwrite(buffer, 512, 1, output);
      }
    }
  }
  fclose(input);
  fclose(output);
  return 0;
}

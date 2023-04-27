#include "helpers.h"
#include <math.h>
#include <stdio.h>

int min(int a, int cap);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
  // loop through the pixels in the image
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      // find the average of the RGB values and round to the nearest integer
      int average = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);
      // set the average value as the new value
      image[i][j].rgbtRed = average;
      image[i][j].rgbtBlue = average;
      image[i][j].rgbtGreen = average;
    }
  }
  return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
  // loop through the pixels of the image
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      // sepia algorithm, if the value is higher than 255 cap the value at 255
      int sepiaRed = min(round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue), 255);
      int sepiaGreen = min(round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue), 255);
      int sepiaBlue = min(round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue), 255);

      // replace the value with new value
      image[i][j].rgbtRed = sepiaRed;
      image[i][j].rgbtGreen = sepiaGreen;
      image[i][j].rgbtBlue = sepiaBlue;
    }
  }
  return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
  // declate temporary variable
  RGBTRIPLE temp[height][width];
  // declare counter that we will use to track the position in our array
  int count = 0;
  // loop through columns
  for (int i = 0; i < height; i++)
  {
    // loop through rows backwards
    for (int j = width - 1; j >= 0; j--)
    {
      // set counter to 0 to avoid segfault and going out of bounds
      if (count == width)
      {
        count = 0;
      }
      // store our values in our temporary array
      temp[i][count] = image[i][j];
      count++;
    }
    // replace image values with reveresed values
    for (int k = 0; k < width; k++)
    {
      image[i][k] = temp[i][k];
    }
  }
  return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  RGBTRIPLE temp[height][width];
  // replace the pixels in the main image
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      temp[i][j] = image[i][j];
    }
  }
  // loop through the image
  for (int k = 0; k < height; k++)
  {
    for (int l = 0; l < width; l++)
    {
      // set initial color values
      float red = 0;
      float blue = 0;
      float green = 0;
      // set pixel count
      int count = 0;
      // loop through the pixels
      for (int m = -1; m <= 1; m++)
      {
        int pixelh = k + m;
        if (pixelh >= 0 && pixelh < height)
        {
          for (int n = -1; n <= 1; n++)
          {
            int pixelw = l + n;
            if (pixelw >= 0 && pixelw < width)
            {
              red += (float)temp[pixelh][pixelw].rgbtRed;
              green += (float)temp[pixelh][pixelw].rgbtGreen;
              blue += (float)temp[pixelh][pixelw].rgbtBlue;
              count++;
            }
          }
        }
      }
      // divide by the amount of pixels counted and round the numbers
      image[k][l].rgbtRed = round(red / count);
      image[k][l].rgbtGreen = round(green / count);
      image[k][l].rgbtBlue = round(blue / count);
    }
  }
  return;
}

// find minimum
int min(int a, int cap)
{
  if (a > cap)
  {
    a = cap;
  }
  return a;
}
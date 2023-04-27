#include "cs50.h"
#include "math.h"
#include "ctype.h"
#include "stdio.h"
#include "string.h"

int calculate_level(string text);

int main()
{
  string text = get_string("Text: ");
  int count = calculate_level(text);

  // print the value
  if (count <= 1)
  {
    printf("Before Grade 1\n");
  }
  if (count >= 16)
  {
    printf("Grade 16+\n");
  }
  if (count > 1 && count < 16)
  {
    printf("Grade %i\n", count);
  }
}

int calculate_level(string text)
{
  char upperCase;
  int countLetters = 0;
  int countWords = 1;
  int countSentences = 0;

  // calculate letters, words and sentences
  for (int i = 0; i < strlen(text); i++)
  {
    upperCase = toupper(text[i]);
    if (upperCase >= 65 && upperCase <= 90)
    {
      countLetters++;
    }
    if (upperCase == ' ')
    {
      countWords++;
    }
    if (upperCase == '!' || upperCase == '.' || upperCase == '?')
    {
      countSentences++;
    }
  }

  // calculate and round the index value
  double L = (float)countLetters / countWords * 100;
  double S = (float)countSentences / countWords * 100;
  double index = round((float)0.0588 * L - 0.296 * S - 15.8);

  return index;
}
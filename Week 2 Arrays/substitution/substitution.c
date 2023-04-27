#include "cs50.h"
#include "math.h"
#include "ctype.h"
#include "stdio.h"
#include "string.h"

int main(int argc, string argv[])
{
  // check if the command line argument contains command
  if (argc != 2)
  {
    printf("Usage: ./substitution key");
    return 1;
  }
  // if the correct number of commands is true
  else if (argc == 2)
  {
    long total = 0;
    int count = 0;
    // loop through the letters in the string
    for (int i = 0; i < strlen(argv[1]); i++)
    {
      char uppercase;
      char c;
      c = argv[1][i];
      // check for more than two the repeating characters
      for (int j = 0; j < strlen(argv[1]); j++)
      {
        char d = argv[1][i + 1];
        if (c == d)
        {
          count++;
        }
      }
      // change each letter to uppercase
      uppercase = toupper(argv[1][i]);
      // calculate the total value of all characters in a string
      total += uppercase;
      // check if the character is a letter in the alphabet
      if (isalpha(c) == 0)
      {
        printf("Key must contain 26 alphabet characters.");
        return 1;
      }
      // check if the key is 26 characters long
      if (strlen(argv[1]) != 26)
      {
        printf("Key must contain 26 characters.");
        return 1;
      }
    }
    // check if there are repeating characters
    if (count > 0)
    {
      printf("Key must not have repeating characters.");
      return 1;
    }
    // 2015 is the total value if there are no more that 2 repeating characters
    if (total != 2015)
    {
      printf("Key must not have repeating characters.");
      return 1;
    }
  }
  else
  {
    return 0;
  }
  string key = argv[1];
  string text = get_string("plaintext: ");
  char cipherchar;
  int number;
  char cipher[1000] = "ciphertext: ";
  for (int i = 0; i < strlen(text); i++)
  {
    cipherchar = text[i];
    // get position of each letter in the alphabet and add to array
    // lowercase
    if (cipherchar >= 97 && cipherchar <= 122)
    {
      number = (cipherchar - 97);
      cipher[12 + i] = tolower(key[number]);
    }
    // uppercase
    if (cipherchar >= 65 && cipherchar <= 90)
    {
      number = (cipherchar - 65);
      cipher[12 + i] = toupper(key[number]);
    }
    // check if the letter is a blank or punctuation
    if (ispunct(cipherchar) || isblank(cipherchar) || isdigit(cipherchar))
    {
      cipher[12 + i] = tolower(cipherchar);
    }
  }
  printf("%s\n", cipher);
}
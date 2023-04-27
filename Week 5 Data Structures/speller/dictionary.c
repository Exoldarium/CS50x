// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <strings.h>
#include <string.h>
#include <stdlib.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
unsigned int counter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int hashedWord = hash(word);
    node *tableWord = table[hashedWord];
    while (tableWord != NULL)
    {
        if (strcasecmp(word, tableWord->word) == 0)
        {
            return true;
        }
        tableWord = tableWord->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dictionaryFile = fopen(dictionary, "r");
    if (dictionaryFile == NULL)
    {
        printf("File not found\n");
    }

    char buffer[LENGTH + 1];

    while (fscanf(dictionaryFile, "%s", buffer) != EOF)
    {
        node *correctWord = malloc(sizeof(node));
        if (correctWord == NULL)
        {
            return 1;
        }
        strcpy(correctWord->word, buffer);
        correctWord->next = NULL;
        unsigned int hashedWord = hash(correctWord->word);
        correctWord->next = table[hashedWord];
        table[hashedWord] = correctWord;
        counter++;
    }
    fclose(dictionaryFile);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *track = table[i];
        node *temp = NULL;
        while (track != NULL)
        {
            temp = track;
            track = track->next;
            free(temp);
        }
    }
    return true;
}

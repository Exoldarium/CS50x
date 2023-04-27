import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py DATABASE SEQUENCE")

    # TODO: Read database file into a variable
    database = []
    subsequence = {}
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            # line["AGATC"] = int(line["AGATC"])
            # line ["AATG"] = int(line["AATG"])
            # line ["TATC"] = int(line["TATC"])
            database.append(line)

    # TODO: Read DNA sequence file into a variable
    sequence = None
    with open(sys.argv[2], "r") as file:
        reader = csv.reader(file)
        for line in reader:
            sequence = line

    # TODO: Find longest match of each STR in DNA sequence
    for i in database[0]:
        if i == "name":
            pass
        else:
            # append the longest match to a new dict and convert to int
            subsequence[i] = (int(longest_match(sequence[0], i)))

    # print(sequence)

    # TODO: Check database for matching profiles
    # convert database values to integers, except names
    for i in range(len(database)):
        for k in database[i]:
            if k == "name":
                pass
            else:
                database[i][k] = int(database[i][k])

    # set counter to 0
    counter = 0
    # default value for person
    person = "No match"
    for i in range(len(database)):
        for j in subsequence:
            # check if key values in dict are the same as in database
            if subsequence[j] == database[i][j]:
                counter += 1
        # if counter is the same as the dict length, we have our person
        if counter == len(subsequence):
            person = database[i]["name"]
            break
        # else reset counter and start again
        else:
            counter = 0

    print(person)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

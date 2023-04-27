# TODO

def main():
    text = input("Text: ")
    count = calculate_level(text)

    if count <= 1:
        print("Before Grade 1")
    if count >= 16:
        print("Grade 16+")
    if count > 1 and count < 16:
        print(f"Grade, {count}")


def calculate_level(text):
    upperCase = None
    countLetters = 0
    countWords = 1
    countSentences = 0

    # calculate letters, words and sentences
    for i in range(len(text)):
        # convert to uppercase
        upperCase = text[i].upper()
        # check if it's a letter, blank or punctuation
        # if so increase count
        if upperCase >= chr(65) and upperCase <= chr(90):
            countLetters += 1
        if upperCase == " ":
            countWords += 1
        if upperCase == '!' or upperCase == '.' or upperCase == '?':
            countSentences += 1

     # calculate and round the index value
    l = float(countLetters / countWords * 100)
    s = float(countSentences / countWords * 100)
    index = round(float(0.0588 * l - 0.296 * s - 15.8))

    return index


main()

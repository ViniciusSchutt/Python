nletters = 0  # Variable to store the number of letters
nwords = 1  # Variable to store the number of words (this variable starts in 1, because there will always be at least one word)
nsentences = 0  # Variable to store the number of sentences
index = 0  # Variable to receive Coleman-Liau index


# Get user text input
text = str(input("Please, write a string of text: "))
text.split(" ")


for i in range(len(text)):
    # Check if the characters is alphanumeric or not
    if text[i].isalpha() and text[i] != '.' and text[i] != '?' and text[i] != '!':
        # If yes, increment the variable number of letters by 1
        nletters += 1

for i in range(len(text)):
    # Check that the character in text[i] is a blank space = ' '
    if text[i].isspace():
        # If it is, increment the number of words by 1
        nwords += 1


for i in range(len(text)):
    # Check if the character in text[i] is an end ('.'), interrogation ('?') or exclamation ('!') point
    if text[i] == '.' or text[i] == '?' or text[i] == '!':
        # If yes, increment the number of sentences by 1
        nsentences += 1


# Calculate the Coleman-Liau index
L = float(nletters / nwords * 100)

S = float(nsentences / nwords * 100)

index = round((float)(0.0588 * L - 0.296 * S - 15.8))

# If the index is between 0 and 16
if index < 16 and index >= 0:
    # Print the grade rounded to the nearest whole number
    print(f"Grade: {round(index)}")

# Else if the index is higher than 16
elif index >= 16:
    # Just print 16+
    print(f"Grade 16+")

else:
    # And if it's less than 1, print 'Before 1'
    print(f"Before Grade 1")



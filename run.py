import random

print("Welcome to Hangman!")
print("--------------------")

# Random words
wordPulp = [
    "monkey", "apple", "computer", "tank",
    "helicopter", "carrot", "sunshine", "elevator"
]

# Choose a random word
randomWord = random.choice(wordPulp)

# Underscores for characters
for x in randomWord:
    print("_", end=" ")

# Hangman design when wrong
    def print_hangman(wrong):
        if wrong == 0:
            print("\n  ----")
            print("     |")
            print("     |")
            print("     |")
            print("     |")
            print("     |")
            print("   -----")
        elif wrong == 1:
            print("\n  ----")
            print("  |  |")
            print("     |")
            print("     |")
            print("     |")
            print("     |")
            print("   -----")
        elif wrong == 2:
            print("\n  ----")
            print("  |  |")
            print("  O  |")
            print("     |")
            print("     |")
            print("     |")
            print("   -----")
        elif wrong == 3:
            print("\n  ----")
            print("  |  |")
            print("  O  |")
            print("  |  |")
            print("     |")
            print("     |")
            print("   -----")
        elif wrong == 4:
            print("\n  ----")
            print("  |  |")
            print("  O  |")
            print(" /|  |")
            print("     |")
            print("     |")
            print("   -----")
        elif wrong == 5:
            print("\n  ----")
            print("  |  |")
            print("  O  |")
            print(" /|| |")
            print("     |")
            print("     |")
            print("   -----")
        elif wrong == 6:
            print("\n  ----")
            print("  |  |")
            print("  O  |")
            print(" /|| |")
            print(" /   |")
            print("     |")
            print("   -----")
        elif wrong == 7:
            print("\n  ----")
            print("  |  |")
            print("  O  |")
            print(" /|| |")
            print(" / | |")
            print("     |")
            print("   -----")


# Print underscores and letters
def printWord(guessedLetters):
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if (char in guessedLetters):
            print(randomWord[counter], end=" ")
            rightLetters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return rightLetters


# Display words underscore
def printUnderscores():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")


# Lenght of word
length_of_word_to_guess = len(randomWord)

# Initialize
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

# Loop
while (amount_of_times_wrong != 7 and
       current_letters_right != length_of_word_to_guess):
    print("\nLetters guessed: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")


# Request input from the user
    letterGuessed = input("\nGuess a letter: ")

# Check if letter already used
    if letterGuessed in current_letters_guessed:
        print("You already guessed this letter", letterGuessed)
        continue

# See if guessed letter is correct
    if (randomWord[current_guess_index] == letterGuessed):
        print_hangman(amount_of_times_wrong)
        current_guess_index += 1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printUnderscores()
    else:
        amount_of_times_wrong += 1
        current_letters_guessed.append(letterGuessed)
        print_hangman(amount_of_times_wrong)
        current_letters_right = printWord(current_letters_guessed)
        printUnderscores()

    if current_letters_right == length_of_word_to_guess:
        print("Congratulations! You guessed the word!:", randomWord)

print("Game Over ")

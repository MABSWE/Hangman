import random

print("Welcome to Hangman!")
print("--------------------")

# Random words
wordPulp = ["monkey", "apple", "computer", "tank", "helicopter", "carrot", "sunshine", "elevator"]

# Choose a random word
randomWord = random.choice(wordPulp)

# Underscores for characters
for x in randomWord:
    print("_", end=" ")

# Hangman design when wrong
def print_hangman(wrong):
    if wrong == 0:
        print("\n----")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("   -----")
    elif wrong == 1:
        print("\n----")
        print("  |  |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("   -----")
    elif wrong == 2:
        print("\n----")
        print("  |  |")
        print("  O  |")
        print("     |")
        print("     |")
        print("     |")
        print("   -----")
    elif wrong == 3:
        print("\n----")
        print("  |  |")
        print("  O  |")
        print("  |  |")
        print("     |")
        print("     |")
        print("   -----")
    elif wrong == 4:
        print("\n----")
        print("  |  |")
        print("  O  |")
        print(" /|  |")
        print("     |")
        print("     |")
        print("   -----")
    elif wrong == 5:
        print("\n----")
        print("  |  |")
        print("  O  |")
        print(" /|\ |")
        print("     |")
        print("     |")
        print("   -----")
    elif wrong == 6:
        print("\n----")
        print("  |  |")
        print("  O  |")
        print(" /|\ |")
        print(" /   |")
        print("     |")
        print("   -----")
    elif wrong == 7:
        print("\n----")
        print("  |  |")
        print("  O  |")
        print(" /|\ |")
        print(" / \ |")
        print("     |")
        print("   -----")

# Print underscores and letters
def printWord(guessedLetters):
    rightLetters = 0
    for char in randomWord:
        if char in guessedLetters:
            print(char, end=" ")
            rightLetters += 1
        else:
            print("_", end=" ")
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
while (amount_of_times_wrong != 7 and current_letters_right != length_of_word_to_guess):
    print("\nLetters guessed: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")
    
# Request input from the user
letterGuessed = input("\nGuess a letter: ")


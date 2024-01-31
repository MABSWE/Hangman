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
        print("/ | \|")
        print("     |")
        print("     |")
        print("   -----")
    elif wrong == 6:
        print("\n----")
        print("  |  |")
        print("  O  |")
        print("/ | \|")
        print(" /   |")
        print("     |")
        print("   -----")
    elif wrong == 7:
        print("\n----")
        print("  |  |")
        print("  O  |")
        print("/ | \|")
        print(" / \ |")
        print("     |")
        print("   -----")
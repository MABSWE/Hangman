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
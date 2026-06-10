import random

# List of predefined words
words = ["apple", "tiger", "chair", "house", "plant"]

# Randomly choose a word
secret_word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong:

    # Display the word with blanks
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player won
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", secret_word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Check correct or wrong
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

# If player loses
if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("The word was:", secret_word)
import random

words = ["apple", "banana", "orange", "grapes", "mango"]
word = random.choice(words)
guessed = "_" * len(word)
tries = 6
guessed_letters = []

print("Welcome to Hangman!")

while tries > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        guessed = "".join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
        print("Correct!")
    else:
        tries -= 1
        print(f"Wrong! Tries left: {tries}")

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nYou lost! The word was:", word)

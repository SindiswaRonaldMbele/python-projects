# Version 3 — Multiple Guesses

secret_word = "hangman"

size = len(secret_word)

guessed = "_" * size

while guessed != secret_word:
    guess = input("Guess the letter: ")
    for k in range(size):
        if (guess in secret_word and secret_word[k] == guess):
            guessed = guessed[:k] + secret_word[k] + guessed[k+1:]
    print(guessed)

# Version 2 — Reveal the Word

secret_word = "hangman"

size = len(secret_word)

guessed = "_" * size


guess = input("Guess the letter: ")
for k in range(size):
    if (guess in secret_word and secret_word[k] == guess):
        guessed = guessed[:k] + secret_word[k] + guessed[k+1:]
print(guessed)

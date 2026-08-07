# Version 1 Requirements

secret_word = "hangman"

guess = input("Guess the letter: ")

if guess in secret_word:
    print("Correct!")
    
else:
    print("Incorrect!")
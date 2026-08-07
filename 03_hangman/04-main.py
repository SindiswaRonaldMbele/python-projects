# Version 5 — Prevent Duplicate Guesses

secret_word = "hangman"
lives = 6

size = len(secret_word)

guessed = "_" * size

while (guessed != secret_word and lives != 0):
    guess = input("Guess the letter: ")
    
    if guess in guessed and guess != "":
        print("You already guessed that letter.")
    
    for k in range(size):
        if (guess in secret_word and secret_word[k] == guess):
            guessed = guessed[:k] + secret_word[k] + guessed[k+1:]
    if guess not in secret_word:
        lives -= 1
    print("Lives remaining: ", lives)    
    print(guessed)

if guessed == secret_word:
    print("Congratulations!")
else:
    print("Game Over! \nThe word was: ", secret_word)    
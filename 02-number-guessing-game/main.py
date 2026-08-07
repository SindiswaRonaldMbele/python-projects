import random

random_number = random.randint(1, 100)
count = 0

while True:
    try:
        guessed_number = int(input("Guess a number between 1 and 100: "))
        count += 1

        if (guessed_number > random_number):
            print("Guess: ", guessed_number, "\nToo high!")
        elif (guessed_number < random_number):
            print("Guess: ", guessed_number, "\nToo low!")
        else:
            print("Guess: ", guessed_number, "\nCorrect! \nYou guessed in ", count, " attempts.")
            break
    except ValueError:
        print("Invalid number.")
    
        
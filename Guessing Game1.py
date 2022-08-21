import random

def guess_number(x):
    random_number = random.randint(0,x)

    guess_count = 1
    max_guess = 4
    guess = 0
    while guess_count <= max_guess:
        guess = int(input(f"Guess a number from 0 to {x}: "))
        guess_count+=guess_count
        
        if guess < random_number:
            print("Too small!!.")
        elif guess > random_number:
            print("Too High!!!.")
        elif guess == random_number:
            #print(f"\U0001F44F")
            print(f"CONGRATULATIONS!!!. YOU GUESSED CORRECTLY..")
            break

    else:
        print(f"You lose!!!!")
        print(f"The random number is {random_number}")

guess_number(10)



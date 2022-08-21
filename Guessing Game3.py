import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess = 0
    guess_count = 1
    max_guess = 5

    while guess_count <= max_guess:
        if  low != high: 
           guess = random.randint(low, high)
        else:
            guess = low #could also be high...
    
        feedback = input(f"\nIs {guess} too low(L) or too high(H) or correct(C)? ").lower()
        guess_count = guess_count + 1

        if feedback == 'l':
            low = guess + 1

        elif feedback == 'h':
            high = guess - 1

        elif feedback == 'c':
            print(f"Computer has guessed right!!!!!!")
            break


    else:
        print("Computer has lost!!!!")
        

computer_guess(10)


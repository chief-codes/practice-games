import random
#import emoji

body_parts = [
    "head",
    "leg",
    "hand",
    "eyes",
    "nose",
    "stomach",
    "thigh",
    "bottock",
    "mouth",
    "ear",
    "armpit",
    "feet",
    "toes",
    "heel",
    "chest",
    "cheeks",
    "back",
    "fingers", 
    "teeth",
    "tongue",
    "muscle",
    "heel",
    "shoulder",
    "penis",
    "vagina",
    "navel",
    "breast",
    "waist",
    "knee"
]


def guess_body_part(body_parts) :
    random_guess = random.choice(body_parts)

    guess_count = 1
    max_guess = 6
    guess = 0
    while guess_count <= max_guess:
        guess = input(f"\nGuess a body part: ")
        guess_count+=guess_count

        if guess == random_guess:
            print(f"\U0001F44F")
            print(f"CONGRATULATIONS!!!!!. YOU GUESSED CORRECTLY....")
            break

        elif guess != random_guess:
            print(f"Wrong Guess. Try again")
            print(f"Hint: Word begins with {random.choice(random_guess[0])}")


    else:
        print(f"You Lose!!!!")
        print(f"The random word is {random_guess}")


guess_body_part(body_parts)

# Rock, Paper, Scissors Game

import random 



def choice():
    computer_choice = ['r','p','s']

    user = input("\nWhat is your choice; (r ) for rock, (p) for paper and (s) for scissors:\n")
    computer = random.choice(computer_choice)

    if user == computer:
        print("It\'s a tie")
        print(f"Computer chose the same")

    elif is_win(user, computer):
        print('You Win!!!!!')
        print(f"Computer chose {computer}")

    else:
        print("'You lose!!!!!'")
        print(f"Computer chose {computer}")


def is_win(player, opponent):
    #return true if player wins 
    #r > s, s > p, p > r

    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or \
        (player == "p" and opponent == "r"):
        return True
    

choice()


import random

option = {"R": "Rock", "P": "Paper", "S": "Scissors"}
key = list(option.keys())   # converts the keys in the dictionary into a list


def user_choice():  # gets user's choice
    while True:
        print("Choose:\n'R' for Rock,\n'P' for Paper or\n'S' for Scissors")
        user = input("Rock Paper Scissors? ").upper()
        if user in key:  # validates user's choice
            break
        else:
            print("Invalid input, try again!!!")
    return user


print("Welcome!!!\nThis is a Rock-Paper-Scissors game.")

while True:
    user = user_choice()
    cpu = random.choice(key)
    print("Player({}):CPU({})".format(option[user], option[cpu]))
    if user == cpu:
        print("It's a tie!!! Try again.")
    elif user == 'R' and cpu == 'S' or user == 'S' and cpu == 'P' or user == 'P' and cpu == 'R':
        print("You win!!!")
        break
    elif user == 'S' and cpu == 'R' or user == 'P' and cpu == 'S' or user == 'R' and cpu == 'P':
        print("You lose!!!")
        break
    else:
        pass

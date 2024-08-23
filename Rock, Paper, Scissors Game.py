#Create a simple game where the user plays against the computer. This project helps you understand conditionals and loops.

import random
Options = "rock", "paper", "scissors"
Play = True
while Play == True:
    Computer = random.choice(Options)
    Player = None
    while Player not in Options:
        Player = input("Enter A Choice (rock, paper or scissors) = ")
        

    print(f"Player = {Player}")
    print(f"Computer = {Computer}")

    if Player == "rock" and Computer == "scissors":
        print("You Win!")
    elif Player == "paper" and Computer == "rock":
        print("You Win!")
    elif Player == "scissors" and Computer == "paper":
        print("You Win!")
    elif Player == Computer:
        print("It's A Tie...")
    else:
        print("You Lose...")
    Again = input("Would You Like To Play The Game Again? (y/n)")
    if Again == "n":
        Play = False


print("Thank You For Playing!")




        







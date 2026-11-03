# In this project we have to create a system that replicate rock paper scissor game.

# here computer will renadomly selecr its choice using random library

# user ll make a choice using input function.


# rule to select the winner

# rock vs paper - paper wins
# paper vs scissor - scissor wins
# scissor vs rock - rock wins
# both same - game tie


import random


game = ['rock','paper','scissor']

computer = random.choice(game)

# print(computer)

user = input("Enter your choice: ")

# print(user)


if user == computer:
    print("Game Tie!!")
elif user == "rock" and computer == 'paper':
    print("Computer wins")
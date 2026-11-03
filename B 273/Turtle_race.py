# Task 1:
# import the turtle lib

import turtle
import random



# Task 2:
# Create a  screen title as Turtle_race 
screen = turtle.Screen()

# How to change the size of screen
screen.setup(width=700, height=400)


# Task 3:
# Create 5 different turtles with different colors

# Adding the feature of list 
player_y = [180,110,10,-90,-180]
all_color = ['red','green','blue','orange','magenta']

all_players = []

for i in range(5):
    player = turtle.Turtle('turtle')
    all_players.append(player)
    player.penup()
    player.goto(-330,player_y[i])
    player.color(all_color[i])

# Task 4:
# Arrange all turtle positioned on left

# player1.penup()
# player1.goto(-330,180)
# player2.penup()
# player2.goto(-330,110)
# player3.penup()
# player3.goto(-330,10)
# player4.penup()
# player4.goto(-330,-90)
# player5.penup()
# player5.goto(-330,-180)

# Task 5:
# Move all the turtles with random speeds

# while True:
#     player1.forward(random.randint(2,6))
#     player2.forward(random.randint(2,6))
#     player3.forward(random.randint(2,6))
#     player4.forward(random.randint(2,6))
#     player5.forward(random.randint(2,6))
game_on = True

while game_on:
    for p in all_players:
        p.forward(random.randint(1,4))
        if p.xcor() > 320:
            game_on = False
            winner = p.color()
            print(f"The winner is {winner[0]}")

    
    

# Task 6:
# find the winner according to the color

screen.mainloop()
import turtle
import random

# Task 1: Create a screen width high height normal
screen = turtle.Screen()
screen.setup(width=600, height=400)


# Task 2: Create 5 players with different colors

player_y = [180,100,0,-100,-180]
all_colors = ['red','blue','green','orange','magenta']
all_player = []

for i in range(5):
    player = turtle.Turtle('turtle')
    player.color(all_colors[i])
    player.penup()
    player.goto(-280,player_y[i])
    all_player.append(player)


# Task 3: Make them arrange on the starting line

# Task 4: Move all of them from left to right
is_on = True

while is_on:
    for players in all_player:
        players.forward(random.randint(1,4))
        if players.xcor() > 250:
            is_on = False
            winner = players.color()
            print(f"The Winner is {winner[0]}")



screen.mainloop()
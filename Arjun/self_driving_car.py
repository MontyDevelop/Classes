import random
import turtle
# "400" "400"


screen = turtle.Screen()
screen.setup(width=400, height=400)
all_player = []

for i in range(3):
    x_value = random.randint(-150, 150)
    y_value = random.randint(-150, 150)
    player = turtle.Turtle('square')
    player.penup()
    player.goto(x_value,y_value)
    all_player.append(player)


# print(x_value)
# print(y_value)

screen.mainloop()
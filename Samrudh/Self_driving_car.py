from turtle import *
import random

screen = Screen()
screen.title("Ai self-driving car")
screen.bgcolor("white")
screen.setup(width=600,height=600)



for i in range(4):
    obstacle = Turtle("square")
    obstacle.penup()
    obstacle.goto(random.randint(-200, 200), random.randint(-200, 200))

# Create a car turtle and move it
# while moving you can control this car using lef and right arrow key

car = Turtle("triangle")
car.color("blue")
car.penup()
car.goto(-200,-200)
def turnleft():
    car.left(15)
def turnright():
    car.right(15)

screen.listen()
screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")

while True:
    car.forward(2)
    x,y = car.position()
    # print(x,y)


    screen.update()


screen.exitonclick()
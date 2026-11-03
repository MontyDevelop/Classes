import random
import turtle


screen = turtle.Screen()
screen.setup(width=1000, height= 500)

all_obstacle = []

for i in range (5):
   ob1 = turtle.Turtle()
   x = random.randint(-300,300)
   y = random.randint(-200,200)
   ob1 = turtle.Turtle('square')
   ob1.penup()
   ob1.goto(x,y)
   all_obstacle.append(ob1)
   


car = turtle.Turtle('triangle')
car.right(180)


is_on = True
while is_on:
   car.forward(2)
   for ob in all_obstacle:
      if car.xcor() > 300 or car.xcor()<-300:
         car.right(180)
      if car.distance(ob)<30:
         print("collision")




screen.mainloop()
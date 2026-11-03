import turtle


# How to create the blank paper to draw on it. 

paper = turtle.Screen()
paper.title("Monty Canvas")



# How to create a pencil to draw the shapes
pencil = turtle.Turtle()

# colors
pencil.pencolor('green')

# shapes
pencil.shape("turtle") # we have only limited number of shapes

# thickness of line
pencil.pensize(10)



# How to draw on screen
# pencil.forward(200)



# square
# pencil.forward(200)
# pencil.left(90)
# pencil.forward(200)
# pencil.left(90)
# pencil.forward(200)
# pencil.left(90)
# pencil.forward(200)
# pencil.left(90)


# Rectangle



# Circle

pencil.circle(100)

# how to stop the turtle not to draw something on paper
pencil.penup()



pencil.forward(200)


pencil.pendown()

pencil.forward(200)
pencil.left(90)
pencil.forward(200)
pencil.left(90)
pencil.forward(200)
pencil.left(90)
pencil.forward(200)
pencil.left(90)



paper.mainloop()
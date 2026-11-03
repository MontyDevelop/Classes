# Graphics


# Animation,drawing


import turtle 

# creating a screen canvas
screen = turtle.Screen()
screen.setup(width=300, height=200)

# its a sprite that can move and draw
arjun = turtle.Turtle()

arjun.color("red")
# to move the sprite in forward direction 
# arjun.forward(100)


# Draw a square
arjun.forward(100)
arjun.left(90)
arjun.forward(100)
arjun.left(90)
arjun.forward(100)
arjun.left(90)
arjun.forward(100)
arjun.left(90)



screen.mainloop()
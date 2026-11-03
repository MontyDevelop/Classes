# from turtle import *
#
# bot = Turtle('turtle')
# screen = Screen()
# screen.title("AI Drawing Project")
#
# def draw_square(size):
#     for i in range(4):
#         bot.forward(size)
#         bot.right(90)
#
# def drawr_ectangle(length, breadth):
#     for i in range(2):
#         bot.forward(length)
#         bot.left(90)
#         bot.forward(breadth)
#         bot.left(90)
#
# def draw_circle(radius):
#     bot.circle(radius)
#
#
# shape = screen.textinput("What should i Draw?", "(square/rectangle/circle): ").lower()
#
# # using if and else call the functions accordingly
#
# if shape == "square":
#     side = screen.textinput(f"length of side of your {shape}", "Side?")
#     draw_square(int(side))
# elif shape == 'rectangle':
#     length = screen.textinput(f"length of side of your {shape}", "Length?")
#     breath = screen.textinput(f"Breadth of side of your {shape}", "Breadth?")
#     drawr_ectangle(int(length), int(breath))
# elif shape == 'circle':
#     radius = screen.textinput(f"radius of the {shape}", "Radius?")
#     draw_circle(int(radius))
#
#
# screen.mainloop()


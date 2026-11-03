import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.title("AI Self-Driving Car with Obstacle Avoidance")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Draw the road
road = turtle.Turtle()
road.speed(0)
road.penup()
road.goto(-200, 250)
road.pendown()
road.pensize(5)

for _ in range(2):  # Draw a rectangle (road boundary)
    road.forward(400)
    road.right(90)
    road.forward(500)
    road.right(90)

road.hideturtle()

# Create the car
car = turtle.Turtle()
car.shape("triangle")
car.color("red")
car.penup()
car.goto(0, -200)
car.setheading(90)  # Point upwards

# Create obstacles
obstacles = []
for _ in range(3):  # Create 3 obstacles
    obs = turtle.Turtle()
    obs.shape("square")
    obs.color("black")
    obs.penup()
    obs.goto(random.randint(-180, 180), random.randint(-150, 200))
    obstacles.append(obs)


# AI: Make the car move forward and avoid obstacles dynamically
def drive():
    car.forward(2)  # Move forward

    # Get car position
    x, y = car.position()

    # AI: If the car reaches the road boundary, turn back inside
    if x > 190:
        car.left(30)
    elif x < -190:
        car.right(30)

    # AI: Check for nearby obstacles and avoid them
    for obs in obstacles:
        if car.distance(obs) < 25:  # If too close to an obstacle
            turn_direction = random.choice([30, -30])  # Random left or right turn
            car.left(turn_direction)
            print("🚨 AI Avoiding Obstacle!")

    # Keep moving
    screen.ontimer(drive, 50)


# Keyboard Controls for Manual Override
def turn_left():
    car.left(20)


def turn_right():
    car.right(20)


# Listen for keyboard input
screen.listen()
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Start the AI car
drive()

# Keep the screen open
screen.mainloop()
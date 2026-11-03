# weight

# height


# weight / height * height


# variables
# Data types
# Data conversion
# operators
# conditional statements


# Task 1: Greet the user using their name 

print("Welcome to BMI Calculator")
name = input("Enter you name here:  ")

print(f"Hi {name} how r u?")
print("To check your BMI (Body mass index) give us some data below ⬇️")

# Task 2: Ask the user their weight and height in float data types with input()

height = float(input("What is your height?: ")) / 100
weight = float(input("what is your current weight?: "))


# BODMAS

# Brackets
# of 

# PEMDAS
# Parenthesis ()
# Exponential **
# Multiplication *
# Division /
# Addition +
# Subtraction -


# Task 3: Create the BMI formula 

BMI = weight/(height * height)
print(round(BMI, 1))


# Task 4: print the result using conditional statements.

if BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 25:
    print("Normal")
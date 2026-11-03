# In this project we are developing a ticket generating system

# person has to pass the eligibility criteria

# age must be equal or over 10
# height must be equal or over 100 cm


# age     price
# 10-20   $2
# 21-30   $2.5
# 31-45   $3
# 46-60   $5

# Task 1: Ask the user their age and check if it is equal or over 10 or not.

# age = int(input("Enter your age (years): "))

# if age >= 10:
#     print("You are eligible.")
# else:
#     print("You r not eligibile.")


# problem: if user enter an unrealistic number like 21444556565656 system says you r eligibile.

# solution: use logical operators


age = int(input("Enter your age (years): "))
if age >= 10 and age <=60:
    print("You are eligible.")
else:
    print("You r not eligibile.")


# Task 2: Do the same with height

height = int(input("Enter your height (cm): "))
if height >= 100 and height <=180:
    print("You are eligible.")
else:
    print("You r not eligibile.")

# Task 3: decide the ticket price based on age and price list


# Task 4: Print a ticket in formatted style

# =========================
# =    Ticket             =
# = Ride: Giant coaster   =
# = Price: $3             =
# =                       =
# =========================

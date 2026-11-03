# variables
# data types
# loop
# list
# conditional statements
# opeartors
# random lib

import random

# Create your version of game logo


# ----------------------------------------------
options = ['rock','paper','scissor']

# comp vs user
comp = random.choice(options)
print(comp)


user = input("Enter 'rock','paper','scissor' (anyone): ")
print(user)



# rock vs paper - paper wins
# paper vs scissor - scissor wins
# rock vs scissor - rock wins

if comp == 'rock' and user == 'paper':
    print(f"{comp} vs {user}")
    print("User is winner")
# elif com


# comparison operators
# logical operators
# Carnival ticket system

# In this projec you have to code a system to generate tickets for a ride.

# The elegibility criteria foe a person to ride the rollar coaster 

# age must be more than 12 years old and should not exceed 60 years 
# height must be more than 100 cms


# Ticket pricing will be as follows:

# age 12 - 18 - $5
# age 18 - 25 - $8
# age 25 - 35 - $10
# age 35 - 60 - $12

# Extra feature you can add but optional 

# if a rider need a photo clicked while riding give them option to pay $2 extra with ticket

print("Hello!Welcome to the carnival ticket system.")
name = input("what is your name? :   ")
print(f"Please answer the following questions we will ask {name}")

age = float(input("what is your age?:  "))
height = float(input("what is your height in cm?: "))/100

if age <12 or age  >60:
    print("you are not eligeble to ride the roller coaster.")
elif age >12 and age <60:
    print("you are at the right age to ride the roller coaster!")

    print("please let us check the data from your height!")

    if  height < 1:
        print("You are not eligeble to ride the roller coaster")
    elif height > 1:
        print("You are tall enough to ride the roller coaster!")

    print("the price of the ticket will be  based on your age")

    if age > 12 and age < 18:
        print("price of ticket = $5")
    elif age >18 and age <25:
        print("price of ticket= $8")
    elif age >25 and age <35:
        print("price of ticket = $10")
    elif age >35 and age <60:
        print("price of ticket = $12")

print(f"thank you for using the system {name}!")
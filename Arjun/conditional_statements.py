# if and else


# a = 20

# if a > 10:
#     print("A is greater than 10")
# else:
#     print("A is less than or equal to 10")

# Arjun  = "pen"

# if Arjun == 'pen':
#     print("Arjun has a pen")
# else:
#     print("Arjun don't have the pen")



# Create a code to decide the variable has a number greater than 3
# c = 4

# Create a code to find the actual winner
# arjun = 'winner'
# Atharv = 'looser'


# -------------------BMI Calculator----------------

weight = input("Enter your weight: ")
height  = input("Enter your height: ")


# convert weight and height into intgers


weight = float(weight)
height = float(height) / 100

BMI = round((weight / height ** 2), 1)
print(BMI)


if BMI <= 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 25:
    print("Normal Weight")


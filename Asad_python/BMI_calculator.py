# In this project we have to create a body mass index calculator (BMI)

# Step 1: Create the complete instructions for the user
print("BMI CALCULATOR")
print("==============")
print("You have to enter your weight and height to get your BMI.")
print("")
# Step 2: Ask the user for their weight (KG) and height (cm)
weight = input("Enter your weight (kg): ")
height = input("Enter your height (cm): ")

weight = int(weight)
height = int(height) / 100

# Step 3: Create the formula of BMI and calculate BMI weight / height * height
BMI = weight/(height*height)

# BODMAS
# PEMDAS

# Step 4: print the BMI with only 2 decimal points maximum.
print(round(BMI, 2))
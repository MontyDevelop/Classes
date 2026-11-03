weight_kg = int(input("Enter your weight: "))
height_cm = int(input("Enter your height: "))/100

BMI = weight_kg / (height_cm**2)

BMI = round(BMI,1)

print(BMI)

# BMI < 18.5  - underweight
# BMI 18.5 to 24.9 - Normal
# BMI 25 to 29.9 Overweight
# BMI 30 to 34.9 - Obesity
# BMI  35 to 39.9 - extreme obesity

# Continious conditional statements

if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal BMI")
elif BMI < 30:
    print("Overweight")
elif BMI < 35:
    print("Obesity")
elif BMI < 40:
    print("extreme obesity")
else:
    print("Invalid Data")


# Home work

# Create a project 


# School grading system

# student has  to enter their subject marks
# add the subject marks and save it in total_mark variable
# 
# if total mark is over 90 its A+ grade
# if total mark is over 80 till 90 its B+ Grade 
# if total mark > 70 till 80 its C+ Grade
# if total amrk is over 50 till 70 its D Grade
# below 50 is fail
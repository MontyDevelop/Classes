# Task 1:
# Give information about your code


# Task 2:
# Ask the student to make a input of marks obtained


# Task 3:
# Using if, elif and else decide the  grade according to their marks

# 90+ A grade
# 75 - 90 B Grade
# 55 - 75 C grade
# 45 - 55 D grade
# below 45 fail


# Task 4:
# Print the result with student name 


# ---------------------------------------------


# Task 1:
# Give information about your code
print("welcome to the grading system!")
print("you can insert your score and receive your grade for that subject")
name = input("what is your name?:  ")

# Task 2:
# Ask the student to make a input of marks obtained
score = float(input("what is the score you have recieved in your chosen subject?:  "))

# Task 3:
# Using if, elif and else decide the  grade according to their marks
# 90+ A grade
# 75 - 90 B Grade
# 55 - 75 C grade
# 45 - 55 D grade
# below 45 fail

if score> 90:
    print(f"{name} your grade is: A")
elif score< 90 and score > 75:
    print("grade: B")
elif score<75 and score> 55:
    print("grade: C")
elif score<55 and score> 45:
    print("grade: D")
else:
    print("Grade: F")

# Task 4:
# Print the result with student name

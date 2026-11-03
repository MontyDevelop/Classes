# 4
# 100
# 400

# 2003


# a = int(input("Enter a number: "))

# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# -----------------------------------------------------------------------------------------------

print("year - 2003 ✅")
print("year - 03 ❌")

print("year - 1997 ✅")
print("year - 97 ❌")

year = int(input("Enter a year in four digits: "))


# To determine if a given year is a leap year, you need to check the following conditions:

# Divisibility by 4: The year must be evenly divisible by 4. If it is not, 
# then it is not a leap year.
# if year % 4 == 0:
#     print("Leap year")



# Divisibility by 100: If the year is evenly divisible by 4, 
# then check if it is also divisible by 100. If it is, then it might not be a leap year.

# ----------nested if---------


# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a Leap year")
#     else:
#         print("------")
# else:
#     print("Not a leap year")
    


# Divisibility by 400: If the year is divisible by both 4 and 100, 
# then check if it is also divisible by 400. If it is, then it is a leap year. If it is not, 
# then it is not a leap year.


# --------------Home work---------------

# create a quiz game using nested if where user has to answer all questions one by one without any wrong answer
# if any wrong answer game will restart.

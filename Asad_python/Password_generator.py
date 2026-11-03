# list
# for loop
# operators (Assignment)
# random lib

import random

# Task 1: Create 3 list of alphabet, numbers and special characters

# "A","a"
# 2
# "!"
alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
             "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z",
             "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
             "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_char = ["!", "@", "#", "$", "%", "&", "_"]


# Task 2:

# test the list using for loop to reach each character
# for i in alphabets:
#     print(i)

# Task 3: test random characters from each list
print(random.choice(alphabets))

# Task 4: Create a empty list here

password = []


# Task 5: Using Task 3 test case and task 2 test case try add the random data in password list

for i in range(5):
    password.append(random.choice(alphabets))

print(password)
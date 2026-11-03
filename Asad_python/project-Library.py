# variables - yes
# Data and its different types  - yes
# type conversion - not yet
# if and else - yes
# operators - yes
# list - yes




# In this project we are creating a small virtual Library for the user
# Task 1:
# Create a list of 7 books names

books = ['The Swiss Familly Robinson','A Wish In The Dark',
         'White Fang','Roll Of Thunder Hear My Cry','The Call Of The Wild',
         'The View From Saturday','The War That Saved My Life']


# Task 2:
# Ask the user what book they want to borrow.
print(" ")
print("Here are our books:")
print(" ")

print("1 ",books[0])
print("2 ",books[1])
print("3 ",books[2])
print("4 ",books[3])
print("5 ",books[4])
print("6 ",books[5])
print("7 ",books[6])

user_choice = input("Would you like to borrow or return?: ").lower()
# user_choice = input("Would you like to borrow or return?: ").upper()
# print(user_choice)

if user_choice == "borrow":
    book = int(input("Enter the book number to choose: "))
    books.pop(book-1)
    print("The New selection is:")
    print(books)

elif user_choice == "return":
    book = int(input("Enter the book number to choose: "))
    books.append(books[book])
    print(books)



for i in range(5):
    user_choice = input("Would you like to borrow or return?: ").lower()
    # user_choice = input("Would you like to borrow or return?: ").upper()
    # print(user_choice)

    if user_choice == "borrow":
        book = int(input("Enter the book number to choose: "))
        books.pop(book-1)
        print("The New selection is:")
        print(books)

    elif user_choice == "return":
        book = int(input("Enter the book number to choose: "))
        books.append(books[book])
        print(books)
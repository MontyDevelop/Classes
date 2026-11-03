# if

# elif

# nested if

# conditions

# decision tree


# Player is good enough 
# yes - what level they are now? 
# no - what level they are now?


user = input("Player is good or not reply in yes or no: ")
level = input("enter the level reply in gold, silver or bronze: ")

if user == 'yes':
    print("ok player is good.")
    if level == "gold":
        print("Player if the best")
    elif level == 'silver':
        print("Player is ok for now")
    elif level == 'bronze':
        print("Player need to do better next time..")
    

# if user == 'no':
#     print("player is not good")


# Home work:
# How we can change the level input only triggered when user say yes.
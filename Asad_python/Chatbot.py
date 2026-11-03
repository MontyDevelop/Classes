# In this project we suppose to create a small chatbot
# that can reply you with the questions we ll programme in it.


# Scenario of working

# User: hey 
# chatbot: hello, what is your name?
# User: Hi, my name is asad.
# chatbot: Hi, Asad how can i help you?
# User: i want to know today's weather.
# chatbot: Today's weather is Temperature is 29 celcius and Humidity is 50%

# ---------------------------------------------------------------------------

# Variables
# Data types
# Comparison opeartors
# if and else
# While loop

# Task 1:
# Questions and answers
Questions = ['What is your name?',
             'Why should you never hold your breath in scuba diving?',
             'Are humans different from animals?',
             'Is the moon made of cheese?',
             'Why do we need to cook and sterilize food and water?',
             'Who made you?']

Answers = ['My name is ChatbotGPT, a "knockoff" of all chatbots and also a small project.',
           'You should never hold your breath in scuba diving because if you go up while holding your breath, the air inside your lungs expands and your lungs could rupture.', 
           'No, Humans are not different from animals no matter how hard we try to pretend that.',
           'No, the moon is not made of cheese.',
           'You need to sterilize food and water because ancient humans decided to abuse fire and ruin our survival skils in the process, making animals laugh at us.',
           'My creator is Asad.']

# Task 2:
# we need to create a while loop that repeat until user enter exit as input

# is_on = True
# while is_on:
#     print("running...")
#     user = input("Do you want to continue or exit: ")
#     if user == 'exit':
#         is_on = False

    # ----------------------------




    # ----------------------------


# Task 3:
# update your while loop to access the questions from list

# a = 0
# while a < len(Questions):
#     print(Questions[a])
#     a += 1

    # ----------------------------




    # ----------------------------


# Task 4:
# update the while loop to let the user repond after every question
# a = 0
# while a < len(Questions):
#     print("Chatbot: ",Questions[a])
#     user = input("User: ")
#     a += 1

    # ----------------------------




    # ----------------------------
# Homework

# Task 5:

# update the while loop to let the user repond after every question with actual answer

a = 0
while a < len(Questions):
    
    user = input("User: ").lower()
    # ----------------------------
    if user == "what is your name?":
        print("Chatbot: ",Answers[0])
    elif user == "why should you never hold your breath in scuba diving?":
        print("Chatbot: ", Answers[1])
    elif user == "are humans different from animals?":
        print("Chatbot: ", Answers[2])
    elif user == "is the moon made of cheese?":
        print("Chatbot: ", Answers[3])
    elif user == "why do we need to cook and sterilize food and water?":
        print("Chatbot: ", Answers[4])
    elif user == " who made you?":
        print("Chatbot: ", Answers[5])
    elif user == "exit":
        break
    else:
        print("I dont know!!")
#     # ----------------------------
    a += 1

# Task 6:
# update the if and else with exit option also


# ---------------if and else----------


# ques = "what is your name?"
# ans = "I am Asad"

# user = input("user: ")
# if user == "what is your name?":
#     print("Chatbot: i am chatbot")
# elif user == "who made u?":
#     print("Chatbot: Asad made me with python")
# else:
#     print("I dont know!!")
    
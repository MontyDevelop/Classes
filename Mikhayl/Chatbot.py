# -----------Including ML libraries----------

import nltk
nltk.download('punkt')

intents = {
    "greeting":['hello','hey','hi','good morning','good evening'],
    'farewell':['bye','goodbye','see you again'],
    'feeling':['how are you','how"s it going','how are you doing'],
    'name':['what is your name','who are you']
}

responses = {
    "greeting":"Hello! How can i assist you today?",
    'farewell':"Goodbye! Have a great day!",
    'feeling':"I'm just a chatbot, but I'm doing great! How about you?",
    'name':"I am advanced chatbot created using python and machine learning!"
}

# Preprocessing the data

all_phrases = []
labels = []

for intent, phrases in intents.items():
    all_phrases.extend(phrases)
    labels.extend([intent] *  len(phrases))

# Simple chatbot without ML and AI
#
# Greet the user.
print("Hi ! I am Chatty, your chatbot friend!")
print("You can talk to me by typing something. To exit, type 'bye'.")

# Create a loop to keep chatting until the user says 'bye'

while True:
    user_input = input("You: ").lower() # Convert input to lowercase for easier comparison
    if user_input == 'hi' or user_input == 'hello':
        print('Chatty: Hello there!')
    elif user_input == 'What can you do for me?' or user_input == 'How can you help?':
        print('Chatty: Not many thing unfortunately I am new project that is developing')
    elif user_input == 'Create a image':
        print('Chatty: Sorry, I am unable to use this feature, perhaps in the future I can have access to this feature')

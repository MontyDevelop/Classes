import nltk
import random
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('popular')

responses = {
    "hello":["hi","hey","hi there","hey there","how are you"],
    "name":["CBA"," im CBA","my name is CBA","my name is CBA yours is","my name is CBA and yours","my name is CBA what about you"],
    "fruit":["apple","pinnaple","lychee","tomato","watermelon","sweetmelon"],
    "color":["red","green blue","maroon","purple","pink","lilac"],
    "country":["india","india","UAE","USA","UK","sweden"],
    }

print(responses.keys())

def get_response(user_input):
  for key, value in responses.items():
    if key in user_input.split(" "):
      return random.choice(value)
  return "Error"

while True:
  user_input = input("You: ")
  if "bye" in user_input:
    print("Good bye!!")
    break
  reply = get_response(user_input)
  print(reply)


default_response = "Hmm.. I don't understand that. Try asking something else."
def get_responses(user_input):
  tokens = word_tokenize(user_input.lower())
  for key in responses:
    if key in tokens:
      return random.choice(responses[key])
  return default_response

while True:
  user_input = input("You: ")
  if "bye" in user_input.lower():
    print("Chatbot: Goodbye! Have a great day..")
    break

  response = get_responses(user_input)
  print(f"Chatbot: {response}")
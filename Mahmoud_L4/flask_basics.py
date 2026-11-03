# web framework

# it ll provide the ready made tools that make it easier to build the web application instead of writing eveything 
# by your own.

# what flask can do ?

# display a webpage in a browser
# respond when someone visits ur website
# recieve the information from users.
# connect a website to python code
# build projects:
    # login system
    # dashboards
    # APIs
    # etc.

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Welcome to my first server in flask"

# @app.route("/robot")
# def robot():
#     return "I am a smart robot..."

# @app.route("/battery")
# def battery():
#     return "Battery level: 85%"


# if __name__ == "__main__":
#     app.run(debug=True)

# name = "Mahmoud"
# __name__ = "Mahmoud"

# ------------------------------------------------------------




from flask import Flask
app =Flask(__name__)

list1=["Where the Wild Things Are",
       "The Very Hungry Caterpillar",
       "Charlotte's Web",
       "Goodnight Moon",
       "The Lion the Witch and the Wardrobe",
       "Matilda",
       "Green Eggs and Ham",
       "Harry Potter and the Philosopher's Stone",
       "Alice's Adventures in Wonderland",
       "Diary of a Wimpy Kid"]

@app.route("/")
def home():
    return "Welcome to our Library"

@app.route("/books")
def books():
    return "<h1>hello</h1>"


if __name__=="__main__":
    app.run(debug=True)

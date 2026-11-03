# Text to speech

import pyttsx3
from tkinter import *

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # female voice (use [0] for male
engine.setProperty('rate', 150)
engine.setProperty('volume',0.6) # 0.0 to 1.0

window = Tk()
window.title("AI That can Speak")
window.geometry('400x200')

# -----------------------------------
label1 = Label(window, text="Type something and click speak!", font=("Arial", 15,'bold'))
label1.pack(pady=10)

entry1 = Entry(window, width=30, font=("Arial", 12,'italic'))
entry1.pack(pady=10)

# -------------------------------------

def speak():
    text = entry1.get()
    if text.strip() != "":
        engine.say(text)
        engine.runAndWait()

# --------------------------------------

button1 = Button(window, text="Speak", font=("Arial", 15,'bold'), command=speak,bg="yellow")
button1.pack(pady=20)

window.mainloop()
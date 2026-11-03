# import pyttsx3
#
# engine = pyttsx3.init()
#
# # Set the voice properties
# engine.setProperty('rate', 150)
# engine.setProperty('volume', 1)
#
# # text = "Hello Mikhayl, I am your AI reader!"
# ai_talk = True
# while ai_talk:
#     text = input()
#     engine.say(text)
#     engine.runAndWait()



from tkinter import *
import pyttsx3

engine = pyttsx3.init()


engine.setProperty('rate', 150)
engine.setProperty('volume', 1)


screen = Tk()
screen.title("Text to Speech")


label1 = Label(screen, text="Enter text:")
label1.grid(column=0, row=0)


entry1 = Entry(screen)
entry1.grid(column=1, row=0)

def Convert():
    text = entry1.get()  # Get text from Entry
    engine.say(text)
    engine.runAndWait()

Button(screen, text="Speak", command=Convert).grid(column=0, row=1)
screen.mainloop()



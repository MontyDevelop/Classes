import pyttsx3
import speech_recognition as sr
from tkinter import *
from tkinter import messagebox
import re

engine = pyttsx3.init()
recogniser = sr.Recognizer()



def summarize_text(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    if len(sentences) <= 2:
        return text  
    else:
        summary = sentences[0]
        if len(sentences) > 2:
            summary += " " + sentences[len(sentences)//2]
        summary += " " + sentences[-1]
        return summary


def text_speak():
    text = text_input.get("1.0", END).strip()
    if text:
        summary = summarize_text(text)
        summary_output.delete("1.0", END)
        summary_output.insert(END, summary)
        engine.say(summary)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "Please enter some text to speak")

def speech_text():
    with sr.Microphone() as source:
        try:
            diary_output.delete("1.0", END) 
            diary_output.insert(END, "Listening...")
            audio = recogniser.listen(source, timeout=5)
            text = recogniser.recognize_google(audio)

            
            diary_output.delete("1.0", END)
            diary_output.insert(END, text)

            
            summary = summarize_text(text)
            summary_output.delete("1.0", END)
            summary_output.insert(END, summary)

        except sr.UnknownValueError:
            diary_output.delete("1.0", END)
            diary_output.insert(END, "Sorry, I could not understand.")
        except sr.RequestError:
            diary_output.delete("1.0", END)
            diary_output.insert(END, "Could not request results.")
        except Exception as e:
            diary_output.delete("1.0", END)
            diary_output.insert(END, f"Error: {str(e)}")

def speak_summary():
    summary = summary_output.get("1.0", END).strip()
    if summary:
        engine.say(summary)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "No summary available to speak")


window = Tk()
window.configure(bg="white")
window.geometry("800x500")
window.title("AI Diary App")

label1 = Label(window, text="Diary Input (Type or Speak)", font=("Arial",12), bg="#dff9d0", fg='black')
label1.place(x=80, y=10)

label2 = Label(window, text="Summary", font=("Arial",12), bg="#ddf9d0", fg='black')
label2.place(x=500, y=10)


text_input = Text(window, width=30, height=10, font=("Arial",12))
text_input.place(x=50, y=50)


diary_output = Text(window, width=30, height=10, font=("Arial",12))
diary_output.place(x=50, y=250)


summary_output = Text(window, width=40, height=15, font=("Arial",12))
summary_output.place(x=420, y=50)

speak_button = Button(window, text="Summarize & Speak (Text)", command=text_speak, bg='green', fg='white', width=20)
speak_button.place(x=70, y=430)

listen_button = Button(window, text="Speak to Text", command=speech_text, bg='blue', fg='white', width=20)
listen_button.place(x=280, y=430)

summary_speak_button = Button(window, text="Read Summary", command=speak_summary, bg='purple', fg='white', width=20)
summary_speak_button.place(x=530, y=430)

window.mainloop()
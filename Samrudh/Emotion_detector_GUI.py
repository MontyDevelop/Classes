import tkinter as tk
from tkinter import messagebox

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

texts = [
    "I am so happy today!",
    "I feel really sad and alone",
    "This is the best day ever",
    "I am angry with you",
    "I love this",
    "I am reading",
    "I am scared of the dark"
]

emotions = ['happy',"sad","happy","angry","happy","neutral","fear"]


model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(texts, emotions)


window = tk.Tk()
window.title("Emotion Detector AI 😊")
window.geometry("400x300")
# window.config(bg="brown")


label = tk.Label(window, text="Tell me how you feel:", font=("Arial", 15)).pack(pady=10)

entry = tk.Entry(window, font=("Arial", 13), width=30).pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial",20)).pack(pady=20)



def detect_emotion():
    sentence = entry.get()
    if sentence.strip() == "":
        messagebox.showwarning("Oops!, Please type something!")
        return
    emotion = model.predict([sentence])[0]
    result_label.config(text=f"{emotion.upper()}")

button = tk.Button(window, text="Detect Emotion", command=detect_emotion, font=("Arial",15)).pack(pady=10)

window.mainloop()

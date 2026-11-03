# In this project we have to create a tkinter GUI
# In this we can use Text to speech and speech to text in a single window

import tkinter as tk
import pyttsx3
import speech_recognition as sr
from tkinter import messagebox

# Initialize TTS engine
engine = pyttsx3.init()

# --- Functions ---

def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "Please enter some text to speak.")

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, "Listening...\n")
            audio = recognizer.listen(source, timeout=5)
            recognized_text = recognizer.recognize_google(audio)
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, recognized_text)
        except sr.WaitTimeoutError:
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, "Listening timed out.")
        except sr.UnknownValueError:
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, "Sorry, I couldn't understand.")
        except sr.RequestError:
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, "Service is unavailable.")

# --- GUI Setup ---

window = tk.Tk()
window.title("Text ↔ Speech Converter")
window.geometry("800x400")
window.config(bg="#f0f0f0")

# --- Frames for side-by-side layout ---
left_frame = tk.Frame(window, bg="#f0f0f0")
right_frame = tk.Frame(window, bg="#f0f0f0")

left_frame.pack(side=tk.LEFT, padx=20, pady=20)
right_frame.pack(side=tk.RIGHT, padx=20, pady=20)

# --- Left: Text to Speech ---
tk.Label(left_frame, text="Text to Speech", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)

text_entry = tk.Text(left_frame, height=10, width=40, font=("Arial", 12))
text_entry.pack(pady=5)

tts_btn = tk.Button(left_frame, text="🔊 Speak Text", command=text_to_speech,
                    bg="#4CAF50", fg="white", font=("Arial", 12))
tts_btn.pack(pady=10)

# --- Right: Speech to Text ---
tk.Label(right_frame, text="Speech to Text", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)

text_output = tk.Text(right_frame, height=10, width=40, font=("Arial", 12))
text_output.pack(pady=5)

stt_btn = tk.Button(right_frame, text="🎤 Speak to Text", command=speech_to_text,
                    bg="#2196F3", fg="white", font=("Arial", 12))
stt_btn.pack(pady=10)

# --- Run the App ---
window.mainloop()

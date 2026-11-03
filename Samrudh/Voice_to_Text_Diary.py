import speech_recognition as sr
from datetime import datetime

def take_user_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio) # local variable
            return f"You Said: {text}"
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio..")
            return None

def save_entry(text):
    now = datetime.now()
    filename = f"diary_{now.strftime('%Y-%m-%d')}.txt"

    with open(filename, 'a') as file:
        file.write(f"\n[{now.strftime('%H:%M:%S')}] {text}")
    print(f"Entry Saved in {filename}")


if __name__ == "__main__":
    spoken_text = take_user_voice()
    if spoken_text:
        save_entry(spoken_text)

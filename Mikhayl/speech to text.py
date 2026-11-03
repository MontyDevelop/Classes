import speech_recognition as sr

# initialize recognizer

recognizer = sr.Recognizer()

# use microphone as the source

with sr.Microphone() as source:
    print("Say Something: ")
    # Listen for audio from microphone
    audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio)
    print(f"You Said: {text}")


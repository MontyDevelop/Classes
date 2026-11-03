import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You Said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio..")


# speech_recognition
# datetime
# os
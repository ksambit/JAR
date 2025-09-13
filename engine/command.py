import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()

import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

@eel.expose

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-ind')
        print(f"User said: {query}")
        eel.DisplayMessage(f"You said: {query}")
        speak(f"You said: {query}")
        eel.ShowHood()
    except Exception as e:
        print("Say that again please...")
        eel.DisplayMessage("Say that again please...")
        return "None"
    return query

def run_query():
    query = takecommand()
    if query == "None":
        return
    # Process the query here        
import os
import time
import speech_recognition as sr
import pyttsx3 #This library is specifically designed to convert text into spoken language, a process known as text-to-speech (TTS).


def speak(text):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    # Initialize speech recognition engine
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print("you said: ", said)
        except Exception as e:
            print("Exception: ", str(e))
    return said.lower()


def open_app (text):
    # Define the application to be opened
    app_name = text
    # Get the path to the application
    app_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\{app_name}\\{app_name}.exe"
    # Open the application
    os.startfile(app_path)
    speak(f"Opening {app_name} for you.")
    
text = get_audio()   
open_app(text)

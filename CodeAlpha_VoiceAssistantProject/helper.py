import os  # provides a collection of functions for interacting with the operating system
import time
import speech_recognition as sr
import pyttsx3
import pytz # This library is essential for handling time zones accurately and reliably in Python.
import subprocess

class communacations:
    def speak(text):  # this is just for tacking text and reading
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""
            try:
                said = r.recognize_google(audio)
                print("You said: ", said)
            except Exception as e:
                print("Exception: ", str(e))
        return said.lower()
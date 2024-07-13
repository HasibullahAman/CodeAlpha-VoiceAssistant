import os #provides a collection of functions for interacting with the operating system
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS


def speak(text): # this is just for tackling text and reading
    tts = gTTS(text=text, lang='en', slow=False)
    filename = 'temp.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
    
speak("Hello, I am Hasibullah Aman and I want to marry with you!")

# import when I get the Google Calendar API
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

import os #provides a collection of functions for interacting with the operating system
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def speak(text): # this is just for tacking text and reading
    tts = gTTS(text=text, lang='en', slow=False)
    filename = 'temp.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.close(filename) # we close mp3 file before the anohter task
    os.remove(filename)
    
speak("Hello, I am Hasibullah Aman and I want to marry with you!")
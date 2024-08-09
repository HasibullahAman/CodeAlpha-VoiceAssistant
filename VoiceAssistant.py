# import when I get the Google Calendar API
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os  # provides a collection of functions for interacting with the operating system
import time
import speech_recognition as sr
import pyttsx3
import pytz # This library is essential for handling time zones accurately and reliably in Python.
import subprocess
import pyautogui
import wikipedia

# inner import
from helper import communacations
from open_app import webAssist, operation , openApplication , aditionally
from startApp import startApp
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("calendar", "v3", credentials=creds)

    return service

# create an instance from communacations class
connect  = communacations
start_assistant = startApp
webAss = webAssist
operation = operation
aditionally = aditionally
Oapp = openApplication
start_assistant.wishMe()
start_assistant.username()

WAKE = "hey Assistant"
SERVICE = authenticate_google()
print("started")

while True:
    print("Listening")
    text = connect.get_audio()
    
    if text.count(WAKE) > 0:
        connect.speak("I am ready")
        text = connect.get_audio()
        
    CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
    for phrase in CALENDAR_STRS:
        if phrase in text:
            date = operation.get_date(text)
            if date:
                operation.get_events(date, SERVICE)
            else:
                connect.speak("I don't understand")

    NOTE_STRS = ["make a note", "write this down", "remember this"]
    for phrase in NOTE_STRS:
        if phrase in text:
            connect.speak("What would you like me to write down?")
            note_text = connect.get_audio()
            operation.note(note_text)
            connect.speak("I've made a note of that.")
    WIKIPEDIA = ["wikipedia","give me some infomation about","who is"]
    for pharse in WIKIPEDIA:
        if pharse in text:
            webAssist.wiki(text)
    YOUTUB = ["open youtube","run youtube","find youtube"]
    for pharse in YOUTUB:
        if pharse in text:
            webAssist.youtube(text)
    GOOGLE = ["open google","run google","find google"]
    for pharse in GOOGLE:
        if pharse in text:
            webAssist.google(text)
    GOOGLEMAP = ["where is","location of","find location of","map","countery"]
    for pharse in GOOGLEMAP:
        if pharse in text:
            webAssist.google_map(text)
    CAMERA = ["camera","take a photo"]
    for pharse in CAMERA:
        if pharse in text:
            Oapp.take_photo()
    HIBERNATE = ["hibernate"]
    for pharase in HIBERNATE:
        if pharse in text:
            operation.make_hibernate()
    SHUTDOWN = ["shutdown",'shut down']
    for pharse in SHUTDOWN:
        if pharse in text:
            operation.make_shutdown()
    RESTART = ["restart"]
    for pharse in RESTART:
        if pharse in text:
            operation.make_restart()
    SIGNOUT = ["signout"] 
    for pharse in SIGNOUT:
        if pharse in text:
            operation.make_signout()
    LOCK = ["lock",'locked'] 
    for pharse in LOCK:
        if pharse in text:
            operation.make_lock()
    MUTE = ['mute', 'muted']
    for pharse in MUTE:
        if pharse in text:
            operation.make_mute()
    SCREAN = ['screenshot','screan']
    for pharse in SCREAN:
        if pharse in text:
            operation.take_screenshot()
    OPEN_APP = ['open', 'run','lunch']
    for pharse in OPEN_APP:
        if pharse in text:
            connect.speak("which application you want?")
            print("listening on application...")
            app = connect.get_audio()
            if "word" in app.split(" "):
                operation.open_app("winword")
            elif "excel" in app.split(" "):
                operation.open_app("excel")
            elif "powerpoint" in app.split(" "):
                operation.open_app("powerpnt")
            elif "publisher" in app.split(" "):
                operation.open_app("pub")
            elif "access" in app.split(" "):
                operation.open_app("msaccess")
            elif "chrome" in app.split(" "):
                operation.open_app("chrome")
            elif "firefox" in app.split(" "):
                operation.open_app("firefox")
            elif "edge" in app.split(" "):
                operation.open_app("edge")
            elif "calculator" in app.split(" "):
                operation.open_app("calc")
            elif "Notepad" in app.split(" "):
                operation.open_app("notepad")
            elif "paint" in app.split(" "):
                operation.open_app("mspaint")
            elif "command prompt" in app.split(" ") or "cmd" in app.split(" "):
                operation.open_app("cmd")
            elif "task manager" in app.split(" "):
                operation.open_app("taskmgr")
            elif "control panel" in app.split(" "):
                operation.open_app("control")
            elif "windows media player" in app.split(" ") or "media playyer" in app.split(" "):
                operation.open_app("wmplayer")
            elif "vlc" in app.split(" "):
                operation.open_app("vlc")
            else:
                connect.speak("I'm sorry, I can't find that application.")
    MUSIC = ["music", "song"]
    for pharse in MUSIC:
        if pharse in text:
            print("listening on music...")
            Oapp.music()
    # aditionally part
    WHO = ["who are you","can I know you?"]
    for pharse in WHO:
        if pharse in text:
            aditionally.who()
    STAT = ["how are you?", "what about you?"]
    for pharse in STAT:
        if pharse in text:
            aditionally.howAreYou()
    NameAssistant = ["what is you name?", "what should I call you?"]
    for pharse in NameAssistant:
        if pharse in text:
            aditionally.assitName()
    WHOMADE = ["who made you?"]
    for pharse in WHOMADE:
        if pharse in text:
            aditionally.whoMade()
    TIME = [" what time is it?","clock","say about time"]
    for pharse in TIME:
        if pharse in text:
            aditionally.time()
    RESPONEtOhOWaREyOU = ["I am fine","I'm fine", "note bad", "it's a good day", "I have a good time"]
    for pharse in RESPONEtOhOWaREyOU:
        if pharse in text:
            aditionally.responeToHowAreYou()
    JOKE = ['joke']
    for pharse in JOKE:
        if pharse in text:
            aditionally.joke()
    EXIT = ["exit app", "close the assistant", "stop","don't listen"]
    for pharse in EXIT:
        if pharse in text:
            aditionally.exitApp()
    GOODmORNING = ['good morning', "morning"]
    for pharse in GOODmORNING:
        if pharase in text:
            aditionally.goodMorning()
    GOODafternoon = ['good afternoon', "afternoon"]
    for pharse in GOODafternoon:
        if pharse in text:
            aditionally.goodAfternoon()
    GOODnight = ['good night', "night"]
    for pharse in GOODnight:
        if pharse in text:
            aditionally.goodNight()
    GOODeVENING = ['good evning',"evening"]
    for pharse in GOODeVENING:
        if pharse in text:
            aditionally.goodEvening()
    LOVE = ["love"]
    for pharse in LOVE:
        if pharse in text:
            aditionally.ILove()
    
    
    
    
            

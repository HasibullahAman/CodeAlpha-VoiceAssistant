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

import os  # provides a collection of functions for interacting with the operating system
import time
import speech_recognition as sr
import pyttsx3
import pytz # This library is essential for handling time zones accurately and reliably in Python.
import subprocess

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
MONTHS = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]


def speak(text):  # this is just for tacking text and reading
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    # tts = gTTS(text=text, lang="en", slow=False)
    # filename = "temp.mp3"
    # tts.save(filename)
    # playsound.playsound(filename)
    # os.close(filename)  # we close mp3 file before the anohter task
    # os.remove(filename)


# speak("Please say everything you want!")


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


def get_events(day, service):
    # Call the Calendar API
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=date.isoformat(),
            timeMax=end_date.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
        speak("No upcoming events found.")
    else:
        speak(f"You have {len(events)} events on this day.")
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])
            start_time = str(start.split("T")[1].split("-")[0])
            if int(start_time.split(":")[0]) < 12:
                start_time += "AM"
            else:
                start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
                start_time += "PM"
                
            speak(event["summary"] + "at" + start_time)


def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today
    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass
    if month < today.month & month != -1:
        year += 1
    if day < today.day & month != -1 & day != -1:
        month += 1
    if (
        month == -1 and day == -1 and day_of_week != -1
    ):  # this conditions simply check if day and month not come in my text
        current_day_of_week = (
            today.weekday()
        )  # we look for day of the week, but if our user said friday, which friday?
        dif = day_of_week - current_day_of_week  # her we check for that!

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7
        return today + datetime.timedelta(dif)
    if month == -1 or day == -1:
        return None
    return datetime.date(month=month, day=day, year=year)


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])
    

WAKE = "hey Assistant"
SERVICE = authenticate_google()
print("started")

while True:
    print("Listening")
    text = get_audio()
    
    if text.count(WAKE) > 0:
        speak("I am ready")
        text = get_audio()
        
    CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
    for phrase in CALENDAR_STRS:
        if phrase in text:
            date = get_date(text)
            if date:
                get_events(date, SERVICE)
            else:
                speak("I don't understand")

    NOTE_STRS = ["make a note", "write this down", "remember this"]
    for phrase in NOTE_STRS:
        if phrase in text:
            speak("What would you like me to write down?")
            note_text = get_audio()
            note(note_text)
            speak("I've made a note of that.")
                


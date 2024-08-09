import wikipedia
import webbrowser
import urllib.parse # for using google map
import os
import pyautogui
import datetime
import pyjokes
import winshell
import subprocess
import pytz # This library is essential for handling time zones accurately and reliably in Python.

# inner import
from helper import communacations

# create an instance from communacations class
connect  = communacations

class webAssist:
    def wiki(text):
        connect.speak("Searching Wikipedia..")
        query = text.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        connect.speak("According to Wikipedia")
        print(results)
        
    def youtube():
        connect.speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
        
    def google():
        connect.speak("Here you go to Google\n")
        webbrowser.open("google.com")
        
    def stackoverflow():
        connect.speak("Here you go to Stack Over flow")
        webbrowser.open("stackoverflow.com")
        
    def google_map(text):
        location = text.replace("where is", "", 1).strip()
        connect.speak("User asked to locate: " + location)  
        url = f"https://www.google.com/maps/place/{urllib.parse.quote(location)}"
        webbrowser.open(url)
        connect.speak(f"Opening {location} on Google Maps.")  # Confirm location
        
        
class openApplication:
    def take_photo():
        connect.speak("Opening your default camera...")
        webbrowser.open("microsoft.windows.camera:")
        connect.speak("Your camera has been opened.")
        
    def music():
        connect.speak("Here you go with music")
        music_dir = "D:\MYSong"
        songs = os.listdir(music_dir)
        print(songs)    
        random = os.startfile(os.path.join(music_dir, songs[1]))
        
        
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
class operation:
    def open_app(app_name):
        pyautogui.hotkey('winleft', 'r')
        pyautogui.typewrite(app_name)
        pyautogui.press('enter')
        connect.speak("Done mester!")
        
    def make_hibernate():
        os.system('shutdown /h')
        connect.speak("System is going to hibernate. Please close all applications.")

    def make_shutdown():
        os.system('shutdown /s')
        connect.speak("System is going to shut down. Please close all applications.")
        
    def make_restart():
        os.system('shutdown /r')
        connect.speak("System is going to restart. Please close all applications.")
        
    def make_signout():
        os.system('shutdown -l')
        connect.speak("System is signing out. Please close all applications.")

    def make_lock():
        os.system('rundll32.exe user32.dll,LockWorkStation')
        connect.speak("System is locking. Please close all applications.")    
    
    def make_mute():
        os.system('rundll32.exe user32.dll,SystemParametersInfo 0x14,0,0,0,0')
        connect.speak("System is muted. Please close all applications.")    

    def take_screenshot():
        pyautogui.hotkey('printscreen')
        connect.speak("it's done, please close check you Default folder")
    
    def empty_resycale():
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        connect.speak("Recycle Bin Recycled")
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
            connect.speak("No upcoming events found.")
        else:
            connect.speak(f"You have {len(events)} events on this day.")
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                print(start, event["summary"])
                start_time = str(start.split("T")[1].split("-")[0])
                if int(start_time.split(":")[0]) < 12:
                    start_time += "AM"
                else:
                    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
                    start_time += "PM"
                    
                connect.speak(event["summary"] + "at" + start_time)


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
  
        
class aditionally:
    def who():
        connect.speak("I am a voice assistant designed by CodeAlpha Team. I am here to help you with various tasks like opening applications, searching for information, and performing simple operations on your computer. I am also capable of answering questions about me and my capabilities.")
  
    def assitName():
        connect.speak("I am named Voice Assistant.")
  
    def whoMade():
        connect.speak("I was developed by CodeAlpha Team, a team of highly skilled and passionate software engineers.")
  
    def time():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        connect.speak(f"Sir, the time is {strTime}")
  
    def howAreYou():
        connect.speak("I am fine, Thank you")
        connect.speak("How are you, Sir")
  
    def responeToHowAreYou():
        connect.speak("It's good to know that your fine")
  
    def exitApp():    
        connect.speak("Thanks for giving me your time")
        exit()    
  
    def joke():
        connect.speak("Your' smile is so beautiful, listen to this")
        connect.speak(pyjokes.get_joke())
  
    def goodMorning():
        connect.speak("Good Morning!, have a fun today")
  
    def goodAfternoon():
        connect.speak("Good Afternoon!, it's look a great day")
  
    def goodEvening():
        connect.speak("Good Evening!, it's a great time to getout")
  
    def goodNight():
        connect.speak("Good Night!, it was a good time to day")
  
    def ILove():
        connect.speak("It's hard to understand for me")   

# import libraries
import pyttsx3
import datetime
import speech_recognition as sr
import shutil
# import modules
from helper import communacations
"""
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
   
"""
# create an instance from communacations class
connect  = communacations

 
class startApp:
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        print(hour) 
        if hour>= 0 and hour<12:
            connect.speak("Good Morning Sir !")
        elif hour>= 12 and hour<18:
            connect.speak("Good Afternoon Sir !")   
        else:
            connect.speak("Good Evening Sir !")  
        connect.speak("I am your Assistant")
        
    
    def username():
        connect.speak("What should i call you sir")
        uname = connect.get_audio()
        connect.speak("Welcome Mister")
        connect.speak(uname)
        columns = shutil.get_terminal_size().columns
        
        print("#####################".center(columns))
        print("Welcome Mr.", uname.center(columns))
        print("#####################".center(columns))
        
        connect.speak("How can i Help you, Sir")  
    



''' # uncomment for testing purposes
start_1 = startApp
start_1.wishMe()
start_1.username()
'''
# import libraries
import pyttsx3
import datetime
import speech_recognition as sr
import shutil
# import modules
from helper import communacations
# create an instance from communacations class
connect  = communacations

 
class startApp:
    def wishMe():
        hour = int(datetime.datetime.now().hour) 
        if hour>= 0 and hour<12:
            connect.speak("Good Morning Sir !")
        elif hour>= 12 and hour<18:
            connect.speak("Good Afternoon Sir !")   
        else:
            connect.speak("Good Evening Sir !")  
        connect.speak("I am your Assistant")
        
    
    def username():
        connect.speak("Welcome Mister")
        columns = shutil.get_terminal_size().columns       
        print("#####################".center(columns))
        print("Welcome Mr.")
        print("#####################".center(columns))
        connect.speak("How can i Help you, Sir")  
    



''' # uncomment for testing purposes
start_1 = startApp
start_1.wishMe()
start_1.username()
'''
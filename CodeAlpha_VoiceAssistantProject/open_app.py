import wikipedia
import webbrowser
import urllib.parse # for using google map
import os




# inner import
from helper import communacations


# import library
# from VoiceAssistant import connect.speak, connect.get_audio



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
    pass

class operation:
    def email(self):
        pass
    def take_photo():
        connect.speak("Opening your default camera...")
        webbrowser.open("microsoft.windows.camera:")
        connect.speak("Your camera has been opened.")
    def hibernate():
        os.system('shutdown /h')
        connect.speak("System is going to hibernate. Please close all applications.")

    def shutdown():
        os.system('shutdown /s')
        connect.speak("System is going to shut down. Please close all applications.")
        
    def restart():
        os.system('shutdown /r')
        connect.speak("System is going to restart. Please close all applications.")
        
    def signout():
        os.system('shutdown -l')
        connect.speak("System is signing out. Please close all applications.")

    def lock():
        os.system('rundll32.exe user32.dll,LockWorkStation')
        connect.speak("System is locking. Please close all applications.")    
    def mute():
        os.system('rundll32.exe user32.dll,SystemParametersInfo 0x14,0,0,0,0')
        connect.speak("System is muted. Please close all applications.")    

    def volume_up():
        pass
    def volume_down():
        pass
    def play_pause():
        pass
    def previous_track():
        pass
    def next_track():
        pass
    def take_screenshot():
        pass
    def open_file():
        pass
    def open_folder():
        pass
    def open_app():
        pass
    def search_engine():
        pass
    def search_website():
        pass
    def translate():
        pass
    def weather():
        pass
    def news():
        pass
    def news_headlines():
        pass
    def calculator():
        pass
    def dict():
        pass
    def currency_converter():
        pass
        # def music():
    #     pass
    
    
class aditionally:
    def who():
        pass
    def stat(): # in case user say I'm ok or good
        pass
    def assitName():
        pass
    def whoMade():
        pass
    def play_Search():
        pass
    
    
    
    
class close():
    def exit():
        pass
    
    


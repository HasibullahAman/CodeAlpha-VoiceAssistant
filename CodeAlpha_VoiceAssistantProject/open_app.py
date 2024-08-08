import wikipedia
import webbrowser
import urllib.parse # for using google map
import os
import pyautogui
import datetime
import pyjokes
import winshell

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
  
        
class aditionally:
    def who():
        connect.speak("I am a voice assistant designed by CodeAlpha Team. I am here to help you with various tasks like opening applications, searching for information, and performing simple operations on your computer. I am also capable of answering questions about me and my capabilities.")
  
    def stat(): # in case user say I'm ok or good
        connect.speak("I am a helpful, user-friendly, and adaptable AI assistant designed by CodeAlpha Team.")
  
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
        connect.speak(pyjokes.get_joke())
  
    def goodMorning():
        connect.speak("Good Morning!")
  
    def goodAfternoon():
        connect.speak("Good Afternoon!")
  
    def goodEvening():
        connect.speak("Good Evening!")
  
    def goodNight():
        connect.speak("Good Night!")
  
    def ILove():
        connect.speak("It's hard to understand for me")   
        
        
# aditionally.joke()
        
# aditionally.time()
    
# def wheather(): 
#     api_key = "Api key"
#     base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
#     connect.speak(" City name ")
#     print("City name : ")
#     city_name = connect.get_audio()
#     complete_url = base_url + "appid =" + api_key + "&q =" + city_name
#     response = requests.get(complete_url) 
#     x = response.json() 
        
#     if x["code"] != "404": 
#         y = x["main"] 
#         current_temperature = y["temp"] 
#         current_pressure = y["pressure"] 
#         current_humidiy = y["humidity"] 
#         z = x["weather"] 
#         weather_description = z[0]["description"] 
#         print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
        
#     else: 
#         connect.speak(" City Not Found ")
        
# wheather()


    
# class close():
#     def exit():
#         pass
    




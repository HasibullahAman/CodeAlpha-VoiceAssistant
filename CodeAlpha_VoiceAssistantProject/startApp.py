from helper import *

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
    
class startApp:
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        print(hour) 
        if hour>= 0 and hour<12:
            speak("Good Morning Sir !")
        elif hour>= 12 and hour<18:
            speak("Good Afternoon Sir !")   
        else:
            speak("Good Evening Sir !")  
        speak("I am your Assistant")
        
    
    def username():
        speak("What should i call you sir")
        uname = get_audio()
        speak("Welcome Mister")
        speak(uname)
        columns = shutil.get_terminal_size().columns
        
        print("#####################".center(columns))
        print("Welcome Mr.", uname.center(columns))
        print("#####################".center(columns))
        
        speak("How can i Help you, Sir")  
    


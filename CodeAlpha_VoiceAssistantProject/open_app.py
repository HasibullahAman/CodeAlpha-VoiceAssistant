import wikipedia

# import library
# from VoiceAssistant import speak, get_audio

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
class webAssist:
    def wiki(text):
        speak('Searching Wikipedia...')
        query = get_audio.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        
    # def youtube(self):
    #     pass
    # def google(self):
    #     pass
    # def stackoverflow():
    #     pass
    # def music():
    #     pass
    # def where(): # search for a location
    #     pass

        


class openApplication:
    pass

class operation:
    def email(self):
        pass
    def camara():
        pass
    def hibernate():
        pass
    def shutdown():
        pass
    def restart():
        pass
    def signout():
        pass
    def lock():
        pass
    def mute():
        pass
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
    
    


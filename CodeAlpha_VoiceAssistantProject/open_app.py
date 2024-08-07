import wikipedia
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
    
    


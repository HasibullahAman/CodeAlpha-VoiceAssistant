import os #provides a collection of functions for interacting with the operating system
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS


def speak(text): # this is just for tacking text and reading
    tts = gTTS(text=text, lang='en', slow=False)
    filename = 'temp.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
    
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
    return said


text = get_audio()

if "hello" in text:
    speak("Hello!, How are you doing, it's timee to speak!")
if "my name is" in text:
    speak("My name is HUA robat!, happy to know you know what can I do for you!?")
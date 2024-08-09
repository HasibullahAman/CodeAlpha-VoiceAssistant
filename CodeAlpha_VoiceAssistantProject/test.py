from helper import communacations
# import wikipedia
import webbrowser
import os
connect = communacations
import pyautogui



def volume():
    os.system("nircmd.exe setaudiovolume 100")
# def volume_up():
#     os.system("nircmd.exe setaudiovolume +100000")
import win32com.client
def volume_up():
    pyautogui.hotkey('volumeup')
def volume_down():
    pyautogui.hotkey('volumedown')

def take_screenshot():
    pyautogui.hotkey('printscreen')
    
def open_app():
    pyautogui.hotkey('winleft', 'r')
    
def search_engine():
    pyautogui.typewrite('google')
    pyautogui.press('enter')
    
def search_website():
    pyautogui.typewrite('wikipedia')
    pyautogui.press('enter')
    
def translate():
    pyautogui.hotkey('winleft', 't')
    
def weather():
    pyautogui.hotkey('winleft', 'w')
    
def news():
    pyautogui.hotkey('winleft', 'n')
def news_headlines():
    pyautogui.hotkey('winleft', 'h')
def calculator():
    pyautogui.hotkey('winleft', 'c')

def currency_converter():
    pyautogui.hotkey('winleft', 'v')




# volume_up()
# volume_down()
# take_screenshot()
def open_word():
    pyautogui.hotkey('winleft', 'r')
    pyautogui.typewrite('winword')
    pyautogui.press('enter')

# open_word()
import subprocess

# def open_word():
#     subprocess.run(["word"])

open_word()


# open_app()





 
 
 
 

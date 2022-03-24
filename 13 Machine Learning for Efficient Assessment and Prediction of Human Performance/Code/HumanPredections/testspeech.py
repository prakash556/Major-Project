import  speech_recognition as sr
import pyttsx3
import re
import webbrowser

r = sr.Recognizer()
with sr.Microphone() as  source:
    print("Say Something")
    audio = r.listen(source)
    print ("TIME OVER, THANX ")
try:
    x = r.recognize_google(audio)
    engine = pyttsx3.init()
    print("TEXT:",x)
    engine.say(x)
    engine.runAndWait()
    term = 'yes'
    words = x.split()

    if term in words:
        print("I am Meghanfox")
        engine.say('call to mr pilla siva prasad')
        engine.runAndWait()
        webbrowser.open("notepad.exe","testurl.py")
        webbrowser.open_new("https://www.youtube.com/watch?v=DeB5N_bH7E8")
    elif x =='no':
        print(" i am from Uyyuru")
    else:
        print("command not found")
except:
    pass;
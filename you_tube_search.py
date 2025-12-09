from unittest import result
import webbrowser as web
from django.template import Engine
import pyttsx3
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def you_youtube_src (term):
    result = "https://www.youtube.com/results?search_query="+ term
    web.open(result)
    speak("here i have found somthing for you ")
    speak("hope it will help you")

    # speak("this is what i found")
    pywhatkit.playonyt(term)
    speak("this video helps you to more")

# you_youtube_src("ok")
    
# from aii import speak


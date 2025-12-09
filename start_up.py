import os
import speech_recognition as sr
from aii import takeCommand
while True:

    wake_up = takeCommand()
    
    if "wake up" in wake_up:
        os.startfile("C:\\Users\\hp\\Desktop\\a.i\\aii.py")
    else:

        print("okkk....")

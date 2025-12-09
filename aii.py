import pyttsx3
import speech_recognition as sr
import datetime
import smtplib
import os
import subprocess as sp
import webbrowser
import wikipedia
import winshell
import pyjokes
from playsound import playsound
import keyboard

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take voice command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Unable to Recognize your voice.")
        return "None"
    return query

# Function to wish based on time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning! Wake up sir, we are in Lonavala. The room temperature is good.")
    elif 12 <= hour < 18:
        speak("Good Afternoon! Sir, we are in Lonavala now, and the temperature is good.")
    else:
        speak("Good Evening! Sir, we are in Lonavala now, and the temperature is good.")

# Function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# Function to set an alarm
def setAlarm():
    speak("Enter the time (HH:MM:SS format):")
    time = input("Enter the time: ")
    while True:
        if datetime.datetime.now().strftime("%H:%M:%S") == time:
            speak("Time to wake up sir!")
            PlaySound('Toofan - KGF Chapter 2.mp3')
            break

# Function to open applications
def openApplication(app):
    if app == "camera":
        sp.run('start microsoft.windows.camera:', shell=True)
    elif app == "cmd":
        os.system('start cmd')
    elif app == "my_pc":
        os.system("explorer.exe")
    elif app == "drive_c":
        os.startfile("C:")
    elif app == "drive_d":
        os.startfile("D:")

# Main functionality
if __name__ == "__main__":
    wishMe()
    speak("If you need anything, I am here for you.")
    
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "hello" in query:
            speak("Hello dear, how are you?")
        
        elif "search on youtube" in query:
            query = query.replace("search on youtube", "").replace("play", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        
        elif "alarm" in query:
            setAlarm()

        elif "shut down" in query:
            speak("Shutting down the system.")
            os.system("shutdown /s /t 1")
        
        elif "cmd" in query:
            openApplication("cmd")
            speak("Command Prompt opened.")

        elif "open the camera" in query:
            openApplication("camera")
            speak("Camera opened.")

        elif "restart" in query:
            speak("Restarting the system.")
            os.system("shutdown /r /t 1")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recipient@example.com"  # Replace with the actual recipient
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry, I am unable to send the email.")

        elif "exit" in query or "take a break" in query:
            speak("Thanks for your time. Goodbye!")
            break
            
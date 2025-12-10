import pyttsx3
import speech_recognition as sr
import datetime
import smtplib
import os
import subprocess as sp
import webbrowser
import wikipedia
import pyjokes
from playsound import playsound
import threading

# ------------------- Initialization ------------------- #
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)  # Female voice
engine.setProperty('rate', 180)  # Faster speech

# ------------------- Text-to-Speech ------------------- #
def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_async(text):
    threading.Thread(target=speak, args=(text,), daemon=True).start()

# ------------------- Voice Command ------------------- #
def takeCommand(timeout=5):
    """Listen and recognize user voice command"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, phrase_time_limit=timeout)
        except sr.WaitTimeoutError:
            return "None"
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        return "None"
    except sr.RequestError:
        speak_async("Check your internet connection")
        return "None"
    return query.lower()

# ------------------- Greetings ------------------- #
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak_async("Good Morning! Wake up sir, we are in Lonavala. The room temperature is good.")
    elif 12 <= hour < 18:
        speak_async("Good Afternoon! Sir, we are in Lonavala now, and the temperature is good.")
    else:
        speak_async("Good Evening! Sir, we are in Lonavala now, and the temperature is good.")

# ------------------- Email Function ------------------- #
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        sender_email = os.getenv("EMAIL_USER")
        sender_pass = os.getenv("EMAIL_PASS")
        server.login(sender_email, sender_pass)
        server.sendmail(sender_email, to, content)
        server.quit()
        speak_async("Email sent successfully.")
    except Exception as e:
        speak_async(f"Failed to send email: {str(e)}")

# ------------------- Alarm Function ------------------- #
def setAlarm():
    speak_async("Enter the alarm time in HH:MM:SS format")
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    speak_async(f"Alarm set for {alarm_time}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            speak_async("Time to wake up sir!")
            playsound('Toofan - KGF Chapter 2.mp3')
            break

# ------------------- Open Applications ------------------- #
def openApplication(app_name):
    apps = {
        "camera": 'start microsoft.windows.camera:',
        "cmd": 'cmd',
        "my_pc": "explorer.exe",
        "drive_c": "C:",
        "drive_d": "D:"
    }
    if app_name in apps:
        if app_name == "cmd":
            os.system("start cmd")
        elif app_name.startswith("drive"):
            os.startfile(apps[app_name])
        else:
            sp.run(f'start {apps[app_name]}', shell=True)
        speak_async(f"{app_name} opened successfully.")
    else:
        speak_async("Application not found.")

# ------------------- Wikipedia Search ------------------- #
def searchWikipedia(query):
    try:
        speak_async("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak_async("According to Wikipedia")
        print(results)
        speak_async(results)
    except Exception:
        speak_async("Sorry, I could not find any results.")

# ------------------- YouTube Search ------------------- #
def searchYouTube(query):
    query = query.replace("search on youtube", "").replace("play", "")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    speak_async("Opening YouTube search results.")

# ------------------- System Commands ------------------- #
def shutdownSystem():
    speak_async("Shutting down the system.")
    os.system("shutdown /s /t 1")

def restartSystem():
    speak_async("Restarting the system.")
    os.system("shutdown /r /t 1")

# ------------------- Main Assistant ------------------- #
def assistant():
    wishMe()
    speak_async("If you need anything, I am here for you.")

    while True:
        query = takeCommand()

        if query == "none":
            continue

        if 'wikipedia' in query:
            searchWikipedia(query)
        elif 'youtube' in query:
            searchYouTube(query)
        elif 'alarm' in query:
            setAlarm()
        elif 'cmd' in query:
            openApplication("cmd")
        elif 'camera' in query or 'open camera' in query:
            openApplication("camera")
        elif 'my pc' in query:
            openApplication("my_pc")
        elif 'drive c' in query:
            openApplication("drive_c")
        elif 'drive d' in query:
            openApplication("drive_d")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak_async(f"Sir, the time is {strTime}")
        elif 'send email' in query:
            speak_async("What should I say?")
            content = takeCommand()
            recipient = "recipient@example.com"
            sendEmail(recipient, content)
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak_async(joke)
        elif 'hello' in query:
            speak_async("Hello! How are you?")
        elif 'shut down' in query:
            shutdownSystem()
            break
        elif 'restart' in query:
            restartSystem()
            break
        elif 'exit' in query or 'take a break' in query:
            speak_async("Thanks for your time. Goodbye!")
            break

# ------------------- Run Assistant ------------------- #
if __name__ == "__main__":
    assistant()

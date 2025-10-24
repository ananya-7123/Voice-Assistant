import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
import time
import requests

r = sr.Recognizer()
engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        speak("Good morning! How can I help you today?")
    elif 12 <= hour < 17:
        speak("Good afternoon! What do you want me to do?")
    elif 17 <= hour < 22:
        speak("Good evening! Hope you had a good day so far.")
    else:
        speak("Hey there! Working late again? What should I do for you?")

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='en-in')
            print(f"You said: {command}\n")
        except sr.UnknownValueError:
            print("Could not understand. Please repeat.")
            return ""
        except sr.RequestError:
            print("Network error.")
            return ""
        return command.lower()

def run_assistant():
    greet_user()
    while True:
        command = listen_command()

        if 'open notepad' in command:
            speak("Opening Notepad.")
            os.system("notepad")

        elif 'open chrome' in command:
            speak("Launching Chrome.")
            os.system("start chrome")

        elif 'open calculator' in command:
            speak("Opening Calculator.")
            os.system("calc")

        elif 'open camera' in command:
            speak("Opening Camera.")
            os.system("start microsoft.windows.camera:")

        elif 'open youtube' in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif 'search' in command:
            speak("What should I search for?")
            query = listen_command()
            speak(f"Searching for {query}.")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif 'play music' in command:
            speak("Playing your favorite tunes.")
            music_dir = "C:\\Users\\Public\\Music"
            os.startfile(music_dir)

        elif 'time' in command:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_now}.")

        elif 'date' in command:
            date_today = datetime.datetime.now().strftime("%A, %d %B %Y")
            speak(f"Today is {date_today}.")

        elif 'joke' in command:
            speak("Why did the computer catch a cold? Because it left its Windows open!")

        elif 'who are you' in command or 'your name' in command:
            speak("I’m TISH, your voice assistant. Always ready to help!")

        elif 'how are you' in command:
            speak("I’m doing great! How about you?")

        elif 'thank you' in command:
            speak("You're always welcome!")

        elif 'exit' in command or 'stop' in command:
            speak("Alright, see you soon. Take care!")
            break

        else:
            speak("Sorry, could you please say that again?")
        time.sleep(0.5)

if __name__ == "__main__":
    print("Voice Assistant started. Say 'exit' to stop.")
    greet_user()
    run_assistant()



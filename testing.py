import speech_recognition as sr
import pyttsx3 
import datetime
import wikipedia
import webbrowser
import os
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print("good morning")
        speak("good morning")
       
    elif 12 <= hour <= 18:
        print("good afternoon")
        speak("good afternoon")
        
    else:
        print("good evening")
        speak("good evening")
        

    speak("I am Neon Sir. How can I help you")
    print("I am Neon Sir. How can I help you?")

def takecommand(timeout=3):
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            try:
                audio = r.listen(source, timeout=timeout)
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-IN")
                print(f"You said: {query}\n")
                return query.lower()
            except sr.WaitTimeoutError:
                print("Timeout occurred. Restarting listening...")
                time.sleep(2)
                continue
            except Exception as e:
                print(e)
                print("Sorry, I didn't catch that. Please say it again.")
                continue
          

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if query == "none":
            continue 
        if 'wikipedia' in query or 'information about' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
            
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\aryas\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'thanks' in query:
            speak("You're welcome")
        elif'bye'in query or 'exit' in query:
            speak('goodbye')
            break
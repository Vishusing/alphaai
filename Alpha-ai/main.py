import pyttsx3 as p
import speech_recognition as sr
import randfacts
import datetime

from selenium_web import *
from apis import *

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return("Good morning")
    elif hour >= 12 and hour < 16: 
        return("Good Afternoon")
    else:
        return("Good Evening")

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

today_date=datetime.datetime.now()
r = sr.Recognizer()

speak("Hello sir, i am Alpha.")
speak(wishme())
speak("today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " And its currently " + (today_date.strftime("%I")) +(today_date.strftime("%M")) + (today_date.strftime("%p")))
speak("What can i do for you???")

# Main loop
while True:
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)

        # Stop condition
        if "stop" in text.lower():
            break

        # Wikipedia search function:
        elif "information" in text:
            speak("you need information related to which topic?")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                topic = r.recognize_google(audio)

                speak(f"Searching {topic} in wikipedia")
                print(f"Searching {topic} in wikipedia")

                # Open Wikipedia and handle information retrieval
                open_wikipedia(f"https://en.wikipedia.org/wiki/{topic}")
        
        # Youtube play functionality:
        elif "play" in text or "video" in text:
            speak("you want me to play which video??")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                video = r.recognize_google(audio)

                speak(f"Playing {video} an youtube")
                print(f"Playing {video} an youtube")
                
                open_youtube(f"https://www.youtube.com/results?search_query={video.replace(' ', '+')}")

        # news Api function
        elif "news" in text:
            speak("On which topic you want to hear news??")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                news_topic = r.recognize_google(audio)
            news(news_topic)

        elif "facts" in text:
           x=randfacts.get_fact()
           print(x)
           speak("Did you know that, "+x)

        elif "jokes" in text:
            speak("On which topic you want to hear jokes??")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                joke_topic = r.recognize_google(audio)
            jokes(joke_topic)
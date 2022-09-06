import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio

engine = pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("good morning")

        elif hour>=12 and hour<18:
            speak("good afternoon")

        else:
            speak("good evening")
        speak(" hello sir how are you, tell me how may i help you")
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said:  {query}\n")

    except Exception as e:

        print("say that again please....")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
      query = takeCommand().lower()

      if 'wikipedia' in query:
          speak('searching wikipedia..')
          query = query.replace("wikipedia")
          results = wikipedia.summary(query,sentences=2)
          speak("according to wikipedia..")
          print(results)
          speak(results)
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
      elif 'open google' in query:
          webbrowser.open("google.com")
      elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")
      elif 'play music' in query:
          webbrowser.open("https://www.jiosaavn.com/song/teri-mitti/SSUxeQxfX3o")
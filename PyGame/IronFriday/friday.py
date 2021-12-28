import os
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
friday = pyttsx3.init()
voice = friday.getProperty("voices")
friday.setProperty("voice",voice[1].id)

def speak(audio):
    print("F.R.I.D.A.Y.:  " + audio)
    friday.say(audio)
    friday.runAndWait()
speak("Hello Sir English")
def time():
    Time = datetime.datetime.now().strftime("%I:%M :%p")
    speak(Time)
def welcome():
    hour = datetime.datetime.now().hour
    if hour >=4 and hour <12 :
        speak("Good Morning Sir")
    elif hour >=12 and hour <18 :
        speak("Good Afternoon Sir")
    elif hour >=18 and hour <24 :
        speak("Good Night Sir")
    speak("How can i help you ?")
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.adjust_for_ambient_noise(source)
        c.pause_threshold=1
        audio = c.listen(source)
    try: 
        query = c.recognize_google(audio,language="en")
        print("Sir English : " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command ")
        query=str(input("Your order is: "))
    return query

if __name__ == "__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        if "youtube" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.youtube.com/results?search_query={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "open video" in query:
            meme = "IronFriday\yeahboy.mp4"
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Friday is quitting sir . Goodbye Boss")
            quit()
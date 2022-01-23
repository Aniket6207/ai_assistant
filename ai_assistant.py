import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Mornig")
    elif hour>=0 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello sir, I am Jarvis, how may i help you")


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
        # print(e)
        print("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
             webbrowser.open("youtube.com")
        elif 'open google'  in query:
            webbrowser.open("google.com")
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strtime}")
        elif 'exit' in query:
            break

    speak("Thank you sir,you can call me whenever you want")
"""You can add any feature  according your preference and need"""
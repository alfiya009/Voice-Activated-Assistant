import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8  # Reduced pause threshold to speed up listening
        # r.energy_threshold = 2  # Minimum energy level for considering speech
        # r.dynamic_energy_threshold = True  # Enable dynamic adjustment of energy threshold
        audio = r.listen(source, timeout=5, phrase_time_limit=10)  # Limit listening time

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "None"
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except Exception as e:
        print(e)  # Print the exception for debugging
        print("Say that again please...")
        return "None"
    return query

import random

def generate_random_number():
    return random.randint(0, 7)


# Generate and print a random number between 1 and 7
# random_number = generate_random_number()
# print("Random number between 1 and 7:", random_number)


if __name__ == '__main__':
    wishMe()
    speak("Hello I am you're presonal  AI here ...!")
    speak("How may i help you")

    # takeCommand()
    # while True:
    if 1:
        query = takeCommand().lower()

        #Logic

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')


        elif 'open gmail' in query:
            webbrowser.open('gmail.com')
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\alfiy\\OneDrive\\Documents\\musicForJarves'
            songs = os.listdir(music_dir)
            print(songs)
            son= generate_random_number()
            os.startfile(os.path.join(music_dir,songs[son]))
        
        elif 'tum mile' in query:
            music_dir = 'C:\\Users\\alfiy\\OneDrive\\Documents\\musicForJarves'
            songs = os.listdir(music_dir)
            print(songs)
            son= generate_random_number()
            os.startfile(os.path.join(music_dir,songs[7]))
        elif 'mera safar' in query:
            music_dir = 'C:\\Users\\alfiy\\OneDrive\\Documents\\musicForJarves'
            songs = os.listdir(music_dir)
            print(songs)
            son= generate_random_number()
            os.startfile(os.path.join(music_dir,songs[4]))

        elif 'janam janam' in query:
            music_dir = 'C:\\Users\\alfiy\\OneDrive\\Documents\\musicForJarves'
            songs = os.listdir(music_dir)
            print(songs)
            son= generate_random_number()
            os.startfile(os.path.join(music_dir,songs[1]))
        elif 'meherbani' in query:
            music_dir = 'C:\\Users\\alfiy\\OneDrive\\Documents\\musicForJarves'
            songs = os.listdir(music_dir)
            print(songs)
            son= generate_random_number()
            os.startfile(os.path.join(music_dir,songs[3]))
        elif 'ek zindagi' in query:
            music_dir = 'C:\\Users\\alfiy\\OneDrive\\Documents\\musicForJarves'
            songs = os.listdir(music_dir)
            print(songs)
            son= generate_random_number()
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'mere naam tu' in query:
            music_dir = 'C:\\Users\\alfiy\\OneDrive\\Documents\\musicForJarves'
            songs = os.listdir(music_dir)
            print(songs)
            son= generate_random_number()
            os.startfile(os.path.join(music_dir,songs[5]))
        elif 'khawab' in query:
            music_dir = 'C:\\Users\\alfiy\\OneDrive\\Documents\\musicForJarves'
            songs = os.listdir(music_dir)
            print(songs)
            son= generate_random_number()
            os.startfile(os.path.join(music_dir,songs[2]))
        elif 'tere rastaa' in query:
            music_dir = 'C:\\Users\\alfiy\\OneDrive\\Documents\\musicForJarves'
            songs = os.listdir(music_dir)
            print(songs)
            son= generate_random_number()
            os.startfile(os.path.join(music_dir,songs[7]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Maam the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\alfiy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


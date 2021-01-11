import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', "")
                talk(command)
                print(command)
    except:
        pass

    return command


def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk("plying" + song)
        pywhatkit.playonyt(song)


run_jarvis()

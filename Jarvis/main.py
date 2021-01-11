import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)


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

    except:
        pass

    return command


def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk("plying" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk('the current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'stop' in command:
        exit(1)

    else:
        talk('Please say the command again')


while True:
    run_jarvis()

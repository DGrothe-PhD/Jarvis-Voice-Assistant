import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import traceback

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class status:
    isRunning = True
    engineUsed = ""


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        status.engineUsed = "YouTube"
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who' in command:
        person = command.replace('who', '')
        status.engineUsed = "wikipedia"
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what' in command:
        person = command.replace('what', '')
        status.engineUsed = "wikipedia"
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'when' in command:
        person = command.replace('when', '')
        status.engineUsed = "wikipedia"
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'where' in command:
        person = command.replace('where', '')
        status.engineUsed = "wikipedia"
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('No, I am in a relationship with wifi')

    elif 'joke' in command:
        status.engineUsed = "pyjokes"
        talk(pyjokes.get_joke())

    elif 'stop listening'.__eq__(command):
        talk('Bye, until next time.')
        status.isRunning = False
    else:
        talk('Sorry but I did not understand')

while status.isRunning:
    print("...")# without it, it didn't stop listening
    try:
        run_jarvis()
    except Exception as e:
        talk(f"Sorry, {status.engineUsed} could not find this.") 
        print(e)
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import datetime
import wikipedia
import pyjokes

#We are creating recognizer listening to voice
listener = sr.Recognizer()

#Sometimes something doesnt work
#Alexa przedstawia się na początku programu
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.say('What can i do for you')
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source: #Źródłem jest mikrofon

            # Sprawdzamy czy gotowa jest alexa do słuchania w kodzie, gdzie sie zatrzymało
            print('Listening...') #Sprawdzamy czy gotowa jest alexa do słuchania w kodzie, gdzie sie zatrzymało
            voice = listener.listen(source,phrase_time_limit=10)
            #listener ma słuchać głosu z źródła
            command = listener.recognize_google(voice)
            command = command.lower()
            # if alexa is mention in command then - print command, else not print
        if 'alexa' in command:
            #Dzięki funkcji talk można zmienić print na talk i alexa powie co powiedziałem do niej poprzez zmienną text
                #Usuwamy alexa z String dzwięku żeby jej nie było wyszukiwania muzyki z nazwą alexa w zmaian pusty string - ale ariana grande song
            command = command.replace('alexa', '')
            talk(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        #usuń play z nagranej command
        song = command.replace('play', '')
        #Powiedz playing + nazwa piosenki - słowo po play
        talk('playing '+ song)
        #dodatek pywahtkit odpali piosenkę na youtube - błąd dodać use_api=True
        pywhatkit.playonyt(song, use_api=True)
        print(song)
    elif 'time' in command:
        #strf string format time %H hour %M minutes %p pm am
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is '+ time)
    #Wikipedia
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk((info))
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        printjoke = pyjokes.get_joke()
        print(printjoke)
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
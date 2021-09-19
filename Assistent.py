import pyttsx3
from time import sleep

class Assistant():
    def __init__(self):
        self.speaker = pyttsx3.init()

    def start_up(self):
        self.speaker.say('Hallo un willkommen zu Devil')
        self.speaker.say('Für Infos bitte einfach den Hilfe Knopf Drücken')
        self.speaker.runAndWait()

    def Hilfe(self):
        self.speaker.say('Also Devil ist ein simpler python browser welcher ein paar packages benutzt')
        sleep(4)
        self.speaker.say('Du kannst weitere infos auf Dem GitHub finden dazu einfach den Dev1l Browser knopf drücken!')
        sleep(4)
        self.speaker.say('Wir haben Nochmal laden dann noch Back und Forward Außerdem einen Aktuellen video encoder!')
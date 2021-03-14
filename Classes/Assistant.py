import pyttsx3
from Classes.DecisionMachine import DecisionMachine


class Assistant:
    user_name = ''
    decision_machine = DecisionMachine()
    engine = pyttsx3.init()

    def call_decision(self, text):
        return self.decision_machine.answer(text)

    def __init__(self, name):
        self.user_name = name

    def answer(self, text):
        answer = self.call_decision(text)
        if answer == 'Tchau ^user_name^, até a próxima!':
            self.speak(answer, write = True)
            return True
        if answer != None:
            self.speak(answer, write = True)
            return False

    def speak(self, text, write = False):
        text = text.replace('^user_name^', self.user_name)
        if write:
            print(text)
        self.engine.say(text)
        self.engine.runAndWait()

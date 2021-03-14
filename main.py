from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json

# Importando a assistente
from Classes.Assistant import Assistant

system_assistant = Assistant('System')
system_assistant.speak('Qual é o seu nome?')

user_assistant = Assistant(input('Qual é o seu nome? '))
user_assistant.speak(f'Olá {user_assistant.user_name}, me pergunte oque você quer saber hoje', write = True)



# Ouvindo o usuário
def listen():
    # Reconhecimento de fala
    model = Model('model')
    rec = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 2048)
    stream.start_stream()

    while True:
        data = stream.read(2048)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            result = json.loads(result)

            if result is not None:
                text = result['text']
                print(text)
                exit_ = user_assistant.answer(text)
                if exit_:
                    exit()

listen()
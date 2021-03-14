import pandas as pd
from datetime import date, datetime
from numpy.random import randint
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import webbrowser
from unidecode import unidecode


def action_exit():
    return 'Tchau ^user_name^, até a próxima!'
    exit()

def find_capital(text):
    country = text.split()[-1]

    df = pd.read_csv('Classes/data/countries.csv')
    if len(df[df['country'] == country]) == 0:
        return f'Não existe um país chamado {country}, no nosso banco de dados. Verique se o nome está correto'
    else:
        capital = str(df[df['country'] == country]['capital'].values[0])
        return f'A capital de {country} é {capital}'

def get_date():
    now = date.today()
    return f'Hoje é dia {now.day} do mês {now.month} do ano {now.year}'

def get_hour():
    hour = datetime.now()
    return f'São {hour.hour} horas e {hour.minute} minutos'

def joke():
    jokes_questions = [
        'Qual o animal mais chique do mundo?',
        'Qual é o peixe que caiu de um prédio?',
        'Oque o martelo falou pro prego?'
        ]
    jokes_answers = [
        'O porco, porquê ele vive num chiqueiro.',
        'É o atum, porque ele escorregou do terraço e fez AAAAAATTTUMMMMM',
        'Ai, se eu te prego, ai ai, se eu te prego.'
        ]

    random_joke = randint(len(jokes_questions))
    final_joke = f'''{jokes_questions[random_joke]}             
    {jokes_answers[random_joke]} HAHAHAHAHAHAHA'''
    return final_joke

def good_reaction():
    return 'Que bom'


def open_url(text):
    possible_inputs = ['abra o', 'abra a', 'procure', 'pesquise', 'quanto', 'quanto é', 'pesquise para mim', 'procure para mim', 'ache', 'responda', 'responda para mim']

    for inp in possible_inputs:
        text = text.replace(inp, '')

    search = text.replace(' ', '+')

    search = unidecode(search)

    url = f'https://www.bing.com/search?q={search}&cvid=428a6b465e34423f8cbdaf2f7e1c5c4a&aqs=edge..69i60l3j69i57j69i60.5743j0j1&FORM=ANNTA1&PC=SMTS'
    

    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    html = urlopen(req, timeout=20).read()

    soup = BeautifulSoup(html, 'html.parser')

    order_results = soup.find('ol', id = 'b_results')
    link = order_results.findChildren('a')[0]
    link = link['href']

    webbrowser.open(link)






# Fim da declaração das funções

def DecisionsData():
    inputs_dict = {
        'exit': [
            'eu quero sair','sair','tchau','shaw','até amanhã'
        ],
        'date_today': [
            'que dia é hoje', 'data de hoje', 'data', 'dia'
        ],
        'hour_now': [
            'que horas são', 'horário', 'horas são', 'que horas', 'horas'
        ],
        'capital_country': [
            'qual a capital','qual é a capital','qual capital','com a capital','a capital'
        ],
        'joke': [
            'me conte uma piada', 'piada', 'quero rir', 'risada', 'quero dar risada'
        ],
        'good_reaction': [
            'eu vou bem', 'ótimo'
        ],
        'open_site': [
            'abra o', 'abra a', 'procure', 'pesquise', 'quanto', 'quanto é', 'procure para mim',
            'pesquise para mim', 'ache', 'responda', 'responda para mim'
        ]
    }
    inputs_dict_new = {}

    for action in inputs_dict:
        for question in inputs_dict[action]:
            inputs_dict_new[question] = action
    
    inputs_dict = inputs_dict_new

    actions_dict = {
        'exit':{
            'parameters': False,
            'function': action_exit
        },
        'capital_country':{
            'parameters': True,
            'function': find_capital
        },
        'date_today':{
            'parameters': False,
            'function': get_date
        },
        'hour_now':{
            'parameters': False,
            'function': get_hour
        },
        'joke':{
            'parameters': False,
            'function': joke
        },
        'good_reaction':{
            'parameters': False,
            'function': good_reaction
        },
        'open_site':{
            'parameters': True,
            'function': open_url
        }
    }

    return inputs_dict, actions_dict

get_hour()
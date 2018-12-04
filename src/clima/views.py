from django.shortcuts import render
import requests


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d1c0ff9b87788235f065660eebc4178a'
    cidade = 'Ribeirão Preto'
    clima_cidade = requests.get(url.format(cidade)).json()

    clima = {
        'cidade': cidade,
        'temperatura': clima_cidade['main']['temp'],
        'descricao': clima_cidade['weather'][0]['description'],
        'icone': clima_cidade['weather'][0]['icon']
    }

    context = {'clima': clima}

    return render(request, 'clima/index.html', context)


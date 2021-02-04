from django.shortcuts import render
import requests

# Create your views here.
def get_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 4,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        print(response.__dict__)
        return '<ошибка на сервере погоды. попробуйте позже>'


def index(request):
    selected_city = ''
    weather = ''
    if request.method == "POST":
        selected_city = request.POST['city']
        weather = get_weather(selected_city)
    context = {
        "city": selected_city,
        "weather": weather
    }
    return render(request, 'register/index.html', context)

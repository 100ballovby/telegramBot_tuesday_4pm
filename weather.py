import requests as r
from datetime import datetime


def get_weather(city):
    key = '639cd74b40221a097d31bc5e64e343ab'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    headers = {
        'q': city.capitalize(),  # пишем город с большой буквы
        'appid': key,
        'lang': 'ru',
        'units': 'metric'
    }
    response = r.get(url, params=headers)
    if response.status_code == 200:  # если подключились к серверу и получили от него информацию
        data = response.json()
        today = datetime.today()
        forecast = []
        for line in data['list']:
            date = datetime.fromtimestamp(line['dt'])
            if date.day == today.day:
                day = {'date': date,
                       'temp': line['main']['temp'],
                       'weather': line['weather'][0]['description']}
                forecast.append(day)
            elif date.day == today.day + 1:
                day = {'date': date,
                       'temp': line['main']['temp'],
                       'weather': line['weather'][0]['description']}
                forecast.append(day)

        return forecast  # возвращаем список с погодой
    else:
        return None


weather = get_weather('Вашингтон')

for day in weather:
    print(datetime.strftime(day['date'], '%d.%m, %H:%M'), day['temp'], day['weather'])


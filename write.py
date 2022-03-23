import requests
from threading import Timer

def update(lat, long):
    str = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid=c00ade2e07b8527a06d0b858815fd0f7'
    r = requests.get(str)
    with open("weather_data.json", "w") as f:
        f.write(r.text)
        print('running')
        f.close()

run = True
def interval():
    update(17, 18)
    if run:
        Timer(2, interval).start()

interval()
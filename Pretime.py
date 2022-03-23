import json, requests
from threading import Timer

def WindSpeedChecking(Wind_Speed):
        WindCondition=''
        if 0<Wind_Speed<13.5:
            WindCondition="Breeze"
        elif 14<Wind_Speed<20:
            WindCondition="Gale"        #Thoda Difficult
        elif 20.5<Wind_Speed<27.5:
            WindCondition="Strong"      #Extremes Difficult
        elif 28<Wind_Speed<31.5:
            WindCondition="Storm"  
            Alert()
        elif 32<Wind_Speed:
            WindCondition="Hurricane"
            Alert()
        print(WindCondition)

def RainChecking(rain):
    raincondition =''
    if 0<rain<7.5:
        raincondition ="Light Rain"
    elif 7.5<rain<30:
        raincondition ="Moderate Rain"
    elif 30<rain<150:
        raincondition ="Heavy Rain"
        Alert()
    elif 150<rain:
        raincondition ="Violent Rain"
        Alert()
    print(raincondition)

def Alert():
    print("****************************************************************")

# 5 day forecast

def update(lat, long):
    str = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid=c00ade2e07b8527a06d0b858815fd0f7'
    r = requests.get(str)
    with open("weather_data_pre.json", "w") as f:
        f.write(r.text)
        print('running')
        ForWind()
        ForRain()
        f.close()

run = True
def interval():
    update(9.30, 76.23)
    if run:
        Timer(60*60*4, interval).start()

def ForWind():
    with open('weather_data_pre.json',"rw") as fd:
        data = json.load(fd)
        d1=data['list']
    for i in range(0,len(data['list'])):
        d2=d1[i]
        d3=d2['wind']
        Speed_Wind =d3['speed']
        print(Speed_Wind)
        WindSpeedChecking(Speed_Wind)

def ForRain():
    with open('weather_data_pre.json', 'rw') as fd1:
        data = json.load(fd1)
        d1=data['list']
    for i in range(0,len(data['list'])):
        d2=d1[i]
        if 'rain' in d2:
            d3=d2['rain']
            rainny=d3['3h']
            RainChecking(rainny)

interval()
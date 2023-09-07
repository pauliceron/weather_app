from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Medellin'

    ApiKey = '9d0c4174e8fb1086e926aceb76b4deca'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    Params ={'q':city,'appid': ApiKey, 'units':'metric'}
    r = requests.get(url=URL, params=Params)
    res = r.json() 
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    humidity = res['main']['humidity']
    country = res['sys']['country']

    time = datetime.datetime.now()

    return render(request, 'climapp/index.html', {'description': description,
    'icon': icon,'temp': temp,'humidity': humidity,'country': country,'city':city, 'time':time })
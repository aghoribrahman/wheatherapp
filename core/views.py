from email.policy import default
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests 

# Create your views here.
def home(request):
    
        API_key = 'a2527a69bd7074687005b9251aabee7a'
        city = request.GET.get('city','rewa')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
        data = requests.get(url).json()
        
        if len(city) > 1:
            payload ={  'city':data['name'],
                            'weather': data['weather'][0]['main'],
                            'icon':data['weather'][0]['icon'],
                            'temprature':int(data['main']['temp'] -273),
                            'pressure': data['main']['pressure'],
                            'humidity':data['main']['humidity'],
                            'description':data['weather'][0]['main'],
                        }

            return render(request,'core/home.html',{'data':payload})
        else:
            return redirect('/') 
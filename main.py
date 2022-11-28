import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()


API_KEY = "9db62067908f965e37adfd1e0fd2be4a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input(Fore.LIGHTMAGENTA_EX+"Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    country = data['sys']['country']
    weather = data['weather'][0]['description']
    main_weather = data['weather'][0]['main']
    temperature_celsius = round(data['main']['temp'] - 273.15)
    temperature_fahrenheit = round(temperature_celsius  * 9/5 + 32)
    temp_feels_like_celsius = round(data['main']['feels_like'] - 273.15)
    temp_feels_like_fahrenheit= round(temp_feels_like_celsius  * 9/5 + 32)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    print(Fore.LIGHTGREEN_EX+"Country:", country)
    print("Weather:", weather)
    print("Temperature:", temperature_fahrenheit, "degrees fahrenheit")
    print("Feels Like:", temp_feels_like_fahrenheit, "degrees fahrenheit")
    print("Air Pressure:", pressure, "millibars")
    print("Humidity:", humidity, "percent")
    print("Wind Speed:", wind_speed, "miles per hour")
else:
    print("An error occured")

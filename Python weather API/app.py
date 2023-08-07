import requests

api_key = '7652e2f50581baff5022ee9b44839390'

user_input = input("Enter city: ")

wea_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if wea_data.json()['cod'] == '404':
    print('City not found')
else:
    weather = wea_data.json()['weather'][0]['main']
    temp = round(wea_data.json()['main']['temp'])
    temp = ((temp-32)*5)//9

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°C") 



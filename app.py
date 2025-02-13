import requests

api_key = "19922b04c821559533d0675600db90ae"
user_input = input("Enter the city: ")

weather_data = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()
print(weather)
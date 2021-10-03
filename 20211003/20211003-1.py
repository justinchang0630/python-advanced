import requests, json

api_key = "2f7671995fd280c1b8c10843d66b3f93"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
units = "metric"
lang = "zh_tw"

send_url = base_url
send_url += "appid=" + api_key
send_url += "&q=" + city_name
send_url += "&units=" + units
send_url += "&lang=" + lang

print("%s\n" % send_url)
response = requests.get(send_url)
info = response.json()

if "main" in info.keys() :
    temp_info = info["main"]
    current_temperature = temp_info["temp"]

    weather_info = info["weather"][0]
    weather_description = weather_info["description"]

    print("City = " + city_name)
    print("Temperature = " + str(current_temperature))
    print("Description = " + str(weather_description))
else:
    print(" City Not Found ")
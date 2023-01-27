import requests

#API Key
apiKey = "INSERT YOUR OWN API KEY from OpenWeather"

#Asking for the city name, so that we can get the "lat" and "lon" information
cityName = input("Enter the city name (must be in the US): ")
city_url = f"http://api.openweathermap.org/geo/1.0/direct?q={cityName},US&limit=1&appid={apiKey}"

#Getting lat and lon info
firstResponse = requests.get(city_url)
if firstResponse.status_code in range(200,290):
    city_data = firstResponse.json()
    lat = city_data[0]["lat"]
    lon = city_data[0]["lon"]
else:
    print(f"Error: {firstResponse.status_code}")

#Weather app
weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}"

secondResponse = requests.get(weather_url)
if secondResponse.status_code in range(200,290):
    weather_data = secondResponse.json()
    tempCelsius = round(weather_data["main"]["temp"] - 273.15, 0)
    tempFahrenheit = round((tempCelsius * 9/5) + 32, 0)
else:
    print(f"Error: {firstResponse.status_code}")


print(f"Temperature for {cityName} is {tempCelsius}°C or {tempFahrenheit}°F")
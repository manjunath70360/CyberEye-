import requests

def get_weather():
    # OpenWeatherMap API endpoint
    url = "http://api.weatherapi.com/v1/forecast.json?key=b2e5718cf1da43ea8fe41631243005&q=hyderabad&days=1&aqi=no&alerts=no"
    

    response = requests.get(url)
    
    if response.status_code == 200:

        weather_data = response.json()
        print(weather_data)

if __name__ == "__main__":

    get_weather()

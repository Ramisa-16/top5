import requests
api_key = '29b0dca0ff5a5907e167e1ae909fa7ab'

def get_weather_data(lat, lon, units='metric', lang='en'):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}&lang={lang}'
    
    #print(f"Making request to: {url}")  
    response = requests.get(url)
    data = response.json()

    #print(f"Response Status Code: {response.status_code}")  
    
    if response.status_code == 200:
        temperature = data['main']['temp']
        weather_condition = data['weather'][0]['description']
        return temperature, weather_condition
    else:
        return f"Error: {data.get('message', 'Failed to retrieve data')}"

latitude = 24.098379
longitude = 90.328712
temperature, weather_condition = get_weather_data(latitude, longitude)

print(f"Temperature: {temperature}°C, Weather Condition: {weather_condition}")

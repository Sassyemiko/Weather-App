import requests

# 🔑 PASTE YOUR API KEY HERE Inside the quotes
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetches weather data from the API."""
    
    # Parameters for the API request
    request_args = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        # Send the request
        response = requests.get(BASE_URL, params=request_args)
        
        # Check if the request was successful (Status Code 200)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
            
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return None

def display_weather(data):
    """Extracts and prints specific weather details."""
    
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    
    print("\n" + "="*30)
    print(f"🌍 Weather in {city}, {country}")
    print("="*30)
    print(f"🌡️  Temperature: {temp}°C")
    print(f"🤔 Feels Like: {feels_like}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️  Condition: {description.capitalize()}")
    print("="*30 + "\n")

def main():
    print("🌤️  Simple Weather App 🌤️")
    
    # Check if API key is still the placeholder
    if API_KEY == "YOUR_API_KEY_HERE":
        print("❌ Error: You need to add your API Key in the code!")
        return

    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()
        
        if city.lower() == 'quit':
            print("👋 Goodbye!")
            break
        
        if not city:
            print("⚠️  Please enter a city name.")
            continue
            
        print("⏳ Fetching data...")
        data = get_weather(city)
        
        if data:
            display_weather(data)
        else:
            print("❌ City not found or API error. Please check the spelling.")

if __name__ == "__main__":
    main()
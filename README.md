# Weather Information Script

This script fetches real-time weather data for a specified city using the OpenWeatherMap API.

## Features
- Retrieves weather information based on user input.
- Uses the OpenWeatherMap API to fetch data.
- Displays the weather details in JSON format.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- `requests` library (install using `pip install requests`)

## Setup & Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/weather-script.git
   cd weather-script
   ```
2. Install dependencies:
   ```sh
   pip install requests
   ```
3. Run the script:
   ```sh
   python weather.py
   ```
4. Enter the city name when prompted to get the weather details.

## API Key
This script uses the OpenWeatherMap API. Replace `api_key` in the script with your valid API key. You can obtain an API key by signing up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

## Example Output
```
Enter the city: London
{'coord': {'lon': -0.1257, 'lat': 51.5085}, 'weather': [...], 'main': {...}, ...}
```

## Notes
- The script fetches weather data in imperial units (Fahrenheit). Modify the `units` parameter in the request URL if you prefer Celsius (`metric`) or Kelvin (`standard`).
- Ensure your API key is valid and not expired.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.




import urllib.request
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def get_data(url):
    """Retrieve JSON data from given URL"""
    request = urllib.request.urlopen(url)
    result = request.read()
    data = json.loads(result)
    return data


# URL for London
url = "https://www.metaweather.com/api/location/44418/"

weather_data = get_data(url)
forecast = weather_data['consolidated_weather']

for day in forecast:
    print(day['applicable_date'])
    print(day['weather_state_name'])
    print(day['the_temp'])
    print()

import json
import urllib.request
import ssl
from datetime import datetime


ssl._create_default_https_context = ssl._create_unverified_context


def get_data(url):
    """Retrieve JSON data from given URL"""
    request = urllib.request.urlopen(url)
    result = request.read()
    data = json.loads(result)
    return data


upcoming_launch_url = "https://api.spacexdata.com/v3/launches/upcoming"
upcoming_launch = get_data(upcoming_launch_url)[0]

launch_data = {
    "Mission": upcoming_launch['mission_name'],
    "Date": upcoming_launch['launch_date_local'],
    "Location": upcoming_launch['launch_site']['site_name_long'],
    "Payload": upcoming_launch['rocket']['second_stage']['payloads'][0]['payload_type']
}

launch_data['Date'] = datetime.fromisoformat(launch_data['Date'])

for item in launch_data:
    print(f"{item}: {launch_data[item]}")

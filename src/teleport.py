import urllib.request
import json
import ssl

# Necessary to remove SSL Errors (possibly due to MacOS certificates)
ssl._create_default_https_context = ssl._create_unverified_context


def get_json(url):
    """Retrieve JSON data from given URL"""
    request = urllib.request.urlopen(url)
    result = request.read()
    data = json.loads(result)
    return data


api_base = "https://api.teleport.org/api/"

# api_url = "https://api.teleport.org/api/cities/geonameid:{2643743}"

city = "london"
city_id = "2643743"
cities_endpoint = f"cities/geonameid:{city_id}"
scores_endpoint = f"urban_areas/slug:{city}/scores"

# Constructing URLs
basic_info_url = f"{api_base}{cities_endpoint}"
scores_url = f"{api_base}{scores_endpoint}"

basic_info_json = get_json(basic_info_url)
scores_json = get_json(scores_url)

# Printing basic information for an area
name = basic_info_json['full_name']
population = basic_info_json['population']
print(f"Name: {name}")
print(f"Population: {population}")

categories = scores_json['categories']

for category in categories:
    name = category['name']
    score = category['score_out_of_10']
    print(f"{name}: {score}")

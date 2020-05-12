import urllib.request
import json
import ssl

# Necessary to remove SSL Errors (possibly due to MacOS certificates)
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://api.teleport.org/api/urban_areas/slug:london/scores"

request = urllib.request.urlopen(url)
result = request.read()
score_data = json.loads(result)

categories = score_data['categories']

chosen_categories = ['Housing', 'Cost of Living', 'Startups']

for category in categories:
    if category['name'] in chosen_categories:
        name = category['name']
        score = category['score_out_of_10']
        print(f"{name}: {score:.2f}")

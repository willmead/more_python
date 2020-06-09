import json
import urllib.request
import ssl

# Necessary for this program to work on my computer
ssl._create_default_https_context = ssl._create_unverified_context

stuff = json.loads(urllib.request.urlopen('https://api.spacexdata.com/v3/launches/upcoming').read())
print(stuff)
print(stuff[0]['mission_name']),
print(list(stuff[0].values())[4])
x = stuff[0]['launch_site']
long = x['site_name_long']
print(long)
print('todo')
thing = stuff[0]['rocket']
thing2 = thing['second_stage']
thing3 = thing2['payloads']
thing4 = thing3[0]
print(thing4['payload_type'])

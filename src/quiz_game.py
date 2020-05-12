import urllib.request
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get_json(url):
    """Retrieve JSON data from given URL"""
    request = urllib.request.urlopen(url)
    result = request.read()
    data = json.loads(result)
    return data

url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean"

questions_data = get_json(url)
score = 0

for question in questions_data['results']:
    print(question['question'])
    answer = input('> ')
    if answer == question['correct_answer']:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print(f"Score: {score}")

print(f"Final Score: {score}/10")

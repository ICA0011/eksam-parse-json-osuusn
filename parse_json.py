import json, requests


def parse_json(url):
    content = json.loads(requests.get(url).text)

    for course in content['courses']:
        if course['name'] == "Scripting languages":
            return course['code']

import json

r=requests.get('http://localhost:3433/')

data = r.json()

sorted_json = json.dumps(data, indent=2)

print(sorted_json)

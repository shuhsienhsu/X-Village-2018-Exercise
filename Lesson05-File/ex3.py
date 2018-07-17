import json

with open('ex3.json') as f:
    data = json.load(f)
    print(json.dumps(data, indent=4))
import json
import requests

with open('music_show.json', 'r', encoding='utf-8') as f:
    title = json.load(f)

print(title[0][2])
import requests
import json

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)

with open('music_show.json', 'w', encoding='utf-8') as f:
    f.write(response.text)

with open('music_show.json', 'r', encoding='utf-8') as g:
    text = json.load(g)

with open('music.txt', 'w', encoding='utf-8') as k:
    for i in range(len(text)):
        k.write(text[i]['title'])
        k.write(':')
        k.write(text[i]['startDate'])
        k.write('~')
        k.write(text[i]['endDate'])
        k.write('\n')
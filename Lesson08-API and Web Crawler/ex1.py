import json
import requests

url = 'https://www.metaweather.com/api/location/search/?query=taipei'
r = requests.get(url)
r.encoding = 'utf-8'

with open('taipeiweather.json', 'w+', encoding='utf-8') as f:
    f.write(r.text)
    f.seek(0)
    text = json.load(f) 
#with open('taipeiweather.json', 'r', encoding='utf-8') as g:
    #text = json.load(g)  

url2 = 'https://www.metaweather.com/api/location/' + str(text[0]['woeid']) + '/2018/07/18/'
r2 = requests.get(url2)
r2.encoding = 'utf-8'
#print(r2.text)

with open('weatherdata.json','w+', encoding='utf-8') as k:
    k.write(r2.text)
    k.seek(0)
    text3 = json.load(k)
    #print(k.read())

#print(len(text2))
print(text3[0]['applicable_date'])
print("Latest weather state:" + text3[0]['weather_state_name'])
#print(text2[0]['weather_state_name'])
#for i in range(len(text2)):
    #if(text2[i]['applicable_date'] == '2018-07-18'):
#print(text2)
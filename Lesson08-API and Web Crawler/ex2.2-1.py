from requests_html import HTMLSession

session = HTMLSession()

response = session.get('http://quotes.toscrape.com/')

elements = response.html.find('div.tags')[0].find('a')

for e in elements:
    print(e.attrs['href'])
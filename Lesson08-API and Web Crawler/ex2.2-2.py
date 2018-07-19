from requests_html import HTMLSession

"""session = HTMLSession()
response = session.get('https://www.imdb.com/title/tt4073790/?ref_=fn_al_tt_1')
director = response.html.find('[itemprop=director] [itemprop=name]')
print('Director:')
print(director[0].text)
print()
actors = response.html.find('[itemprop=actor] [itemprop=name]')
print('Actors:')
for actor in actors:
    print(actor.text)"""

session2 = HTMLSession()
response02 = session2.get('https://www.imdb.com/movies-coming-soon/2018-08/')
director02 = response02.html.find('[class="list_item even"] [itemprop=director] [itemprop=name] [itemprop=url]')

print(director02[0].text)


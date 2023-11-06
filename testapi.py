import requests
import pprint
url = 'https://api.hh.ru/vacancies'

data = []

#for page_num in range(1, 6):
response = requests.get(url, params={'page': 1}).json()
response2 = requests.get(url, params={'page': 2}).json()

response.update(response2)

pprint.pprint(response['items'][10])
import requests
from bs4 import BeautifulSoup
import pickle

plazma_tvs = []
base_url = "https://www.jofogas.hu/magyarorszag/plazma"

limit = 2

for i in range(1, limit+1):
    url = f"{base_url}?o={i}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.findAll('div', class_='list-item')

    for cnt, result in enumerate(results):
        tv = {}
        title_object = result.find('h3', class_='item-title')
        tv['id'] = cnt
        tv['name'] = title_object.text.strip()
        tv['url'] = title_object.find('a', href=True)['href']
        tv['price'] = 1000
        plazma_tvs.append(tv)


print(len(plazma_tvs))

with open('plazmatvs.pickle', 'wb') as f:
    pickle.dump(plazma_tvs, f)
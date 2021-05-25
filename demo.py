import requests
from bs4 import BeautifulSoup

URL = 'http://localhost:8000/simple.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('p', class_='outer-text')
print(len(results))
for result in results:
    print(result.prettify())